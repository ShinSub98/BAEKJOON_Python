//유저 정보 불러오기
const access_token = localStorage.getItem("access_token");
fetch('https://ganzi-tkzxf.run.goorm.site/member/info/', {
    method: 'GET',
    headers: {
        'Authorization': `Bearer ${access_token}`
    }
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch((error) => {
    console.error('Error:', error);
    });

//홈 화면에서 랭킹 출력
fetch('https://ganzi-tkzxf.run.goorm.site/member/rank/', {
    method: 'GET',
    headers: {
        'Authorization': `Bearer ${access_token}`
    }
    })
 // 실제 URL로 대체하세요.
    .then(response => response.json())
    .then(data => {
        console.log(data);
        const rankArea = document.querySelector('.mini_rank_area');
        const rankList = data.data.rank_list;
        const medalSrc = ['../images/gold.png', '../images/silver.png', '../images/bronze.png'];

        rankList.slice(0, 4).forEach((user, index) => {
            const userDiv = document.querySelector(`.mini_rank_user:nth-child(${index + 1})`);

            const profileImg = userDiv.querySelector('.profile img');
            // profileImg.src = user.profile_image;
            profileImg.classList.add('img-circle');
            profileImg.src = `https://ganzi-tkzxf.run.goorm.site${user.profile_image}`;

            const medalDiv = userDiv.querySelector('.medal');
            if (medalDiv && medalSrc[index]) {
                const medalImg = medalDiv.querySelector('img');
                medalImg.src = medalSrc[index];
            }

            const nameDiv = userDiv.querySelector('.name');
            nameDiv.textContent = user.nickname;

            const pointRankDiv = userDiv.querySelector('.point_rank');
            pointRankDiv.textContent = `${user.point}p`;
        });
    })
    .catch(error => console.error('Error:', error));
