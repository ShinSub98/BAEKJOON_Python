//미션 고유 아이디 부여하기 + 서버에서 데이터 받아와서 출력.
fetch('https://ganzi-tkzxf.run.goorm.site/mission/')
.then(response => response.json())
.then(data => {

  let misBoxes = document.querySelectorAll('.mis_box'); // 'mis_box' 클래스를 가진 모든 요소를 선택합니다.
  misBoxes.forEach(function(misBox, index) { // 각 'mis_box'에 대해 함수를 실행합니다.
    if (data[index]) { // 반환된 데이터가 해당 인덱스에 있는 경우
      let pic = misBox.querySelector('.pic img');
      let point = misBox.querySelector('.point');
      let misText = misBox.querySelector('.mis_text');

      misBox.id = data[index].mission_id;
      pic.src = data[index].mission_logo; // 이미지의 src를 서버에서 받아온 데이터로 변경합니다.
      point.innerText = data[index].point + 'p'; // point의 텍스트를 서버에서 받아온 데이터로 변경합니다.
    //   misText.innerText = data[index].title; // mis_text의 텍스트를 서버에서 받아온 데이터로 변경합니다.
    // mission title은 서버에서 받아온 데이터로 바꾸니까, 줄바꿈이 적용이 안되어서 안했습니당..

    // 'mis_box' div를 클릭하면 다음 페이지로 이동하고, div의 ID를 쿼리 파라미터로 넘깁니다.
    // 'mis_box' div를 클릭하면 다음 페이지로 이동하고, div의 ID를 쿼리 파라미터로 넘깁니다.
      misBox.addEventListener('click', function(e) {
        // 인증한 미션인 경우
        console.log(1);
        if (this.style.backgroundColor == "gainsboro") {
          e.preventDefault(); // 기본 액션 막기
          alert('이미 인증한 미션입니다.');
        } else {
          // 인증하지 않은 미션인 경우
          window.location.href = './mis_click.html?mission_id=' + this.id;
        }
      });
    }
  });
})
.catch(error => console.log('Error:', error)); // 에러 처리

//인증한 미션은 이미지 바꿔주기
const access_token = localStorage.getItem("access_token");
fetch('https://ganzi-tkzxf.run.goorm.site/mission/completed/list', {
    method: 'GET',
    headers: {
    'Authorization': `Bearer ${access_token}`
    }
    })
    .then(response => response.json())
    .then(data => {//인증한 미션 리스트를 반복문 돌면서, 인증한 미션의 misbox를 선택해 이미지 변경.
        for (let i = 0; i < data.length; i++) {
            // console.log(data[i].mission)
            let div = document.getElementById(data[i].mission);
            let point = div.querySelector('.point');
            let image = div.querySelector('.pic img');
            div.style.backgroundColor="Gainsboro";
            point.style.background="DarkGray";
            point.innerText = "인증 완료";
            image.src = "../images/check.png"
        }
    })