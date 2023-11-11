//유저 정보 불러오기
const access_token = localStorage.getItem("access_token");
fetch('https://ganzi-tkzxf.run.goorm.site/member/rank/', {
    method: 'GET',
    headers: {
        'Authorization': `Bearer ${access_token}`
    }
    })
    .then(response => response.json())
    .then(result => {
        //자신의 프로필, 닉네임, 포인트, 등수, 상위 퍼센테이지 출력
        let myRank = document.querySelector('.my_rank_area');
        let myImage = document.querySelector('.myprofile img');
        let myName = myRank.querySelector('.myname');
        let myPoint = myRank.querySelector('.mypoint');
        let myDeung = myRank.querySelector('.deung');
        let myPer = myRank.querySelector('.sangwe');
        
        // myImage.src = result.data.user.profile_image;
        myImage.src = `https://ganzi-tkzxf.run.goorm.site${result.data.user.profile_image}`;
        myImage.classList.add('img-circle');
        myName.innerText = result.data.user.nickname;
        myPoint.innerText = result.data.user.point + 'p';
        myDeung.innerText = result.data.user.rank + '등';
        myPer.innerText = '상위 ' + result.data.user.percentage + '%';

        //전체 랭킹 출력.
        let rankList = result.data.rank_list;
        let rankListBox = document.querySelector('.rank_list_box');

        rankList.forEach(user => {
            console.log(user);
            //rank_list_box 만들기
            let rankBox = document.createElement('div');
            rankBox.className = 'rank_list_box';
            //랭킹
            let rankDiv = document.createElement('div');
            rankDiv.className = 'rank';
            rankDiv.innerText = user.rank;
            //프로필 이미지
            let profileDiv = document.createElement('div');
            profileDiv.className = 'profile';
            let img = document.createElement('img');
            // img.src = user.profile_image;
            img.classList.add('img-circle');
            img.src = `https://ganzi-tkzxf.run.goorm.site${user.profile_image}`;
            profileDiv.appendChild(img);

            let nameDiv = document.createElement('div');
            nameDiv.className = 'name';
            nameDiv.innerText = user.nickname;

            let pointDiv = document.createElement('div');
            pointDiv.className = 'point';
            pointDiv.innerText = user.point + 'p';

            let line = document.createElement('div');
            line.className = 'greenLine';

            rankBox.appendChild(rankDiv);
            rankBox.appendChild(profileDiv);
            rankBox.appendChild(nameDiv);
            rankBox.appendChild(pointDiv);
            

            var parentElement = document.querySelector(".ranking_area");
            parentElement.appendChild(rankBox);
            parentElement.appendChild(line);
        })
    })
    .catch((error) => {
    console.error('Error:', error);
    });