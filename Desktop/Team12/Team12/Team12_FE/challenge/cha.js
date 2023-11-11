//현재 참가 가능한 챌린지
fetch('https://ganzi-tkzxf.run.goorm.site/challenge/list/pre/')
.then(response => response.json())
.then(data => {
    console.log(data);
    let chaBoxes = document.querySelectorAll('.cha_box'); // 'mis_box' 클래스를 가진 모든 요소를 선택합니다.
    console.log(chaBoxes);
    chaBoxes.forEach(function(chaBox, index) { // 각 'mis_box'에 대해 함수를 실행합니다.
        chaBox.addEventListener('click', function(e) {
            window.location.href = './cha_click.html';
        });
  });
})
.catch(error => console.log('Error:', error)); // 에러 처리