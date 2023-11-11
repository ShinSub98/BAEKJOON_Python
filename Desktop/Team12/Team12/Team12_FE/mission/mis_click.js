// 입력, 출력div 가져옴
const fileInput = document.getElementById("fileInput");
const outputDiv = document.getElementById("output");

// 파일이 선택시 이벤트리스너
fileInput.addEventListener("change", function () {
  // 파일 선택 확인
  if (fileInput.files.length > 0) {
    // 이미지 파일 확인
    const file = fileInput.files[0];
    if (file.type.startsWith("image/")) {
      // FileReader:이미지 출력 div에 추가
      const fileReader = new FileReader();
      fileReader.onload = function (e) {
        // 이미지 출력 + 원본 비율 유지 + 꽉차게
        outputDiv.innerHTML = `<img src="${e.target.result}"  style="width:100%;
        height:100%; object-fit:cover; alt="Uploaded Image">`;
      };

      // 이미지 파일 읽어옴
      fileReader.readAsDataURL(file);
    } else {
      // 이미지 파일 아닌 경우
      outputDiv.textContent = "이미지 파일을 선택해주세요.";
    }
  } else {
    // 파일 선택 안 될 경우
    outputDiv.textContent = "파일을 선택해주세요.";
  }
});

//이전 페이지에서 넘겨준 미션 아이디 받아오기
let params = new URLSearchParams(window.location.search);
let misBoxId = params.get('mission_id');
//헤더에 넘겨줄 access token
const access_token = localStorage.getItem("access_token");
console.log(access_token);

const form = document.getElementById('form')
form.addEventListener('submit', (e) => {
  e.preventDefault();

  const misForm = new FormData(form);
  
  if (misForm){
    misForm.append('mission', misBoxId);

    fetch(`https://ganzi-tkzxf.run.goorm.site/mission/${misBoxId}/completed/`, {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${access_token}`
        },
          body: misForm
        })
        .then(response => response.json())
        .then(data => {
          console.log(data);
          // window.location.href = './mis.html';
          window.location.href = './mis.html?refresh=true';
        }) // 서버의 응답을 콘솔에 출력.
        .catch(error => console.log('Error:', error)); // 에러 처리
  }
});