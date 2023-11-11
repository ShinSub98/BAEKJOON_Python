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

//인증하기 눌렀을 때 스탬프 찍히는거

document.addEventListener("DOMContentLoaded", function () {
  // "div class="inzug"" 요소를 가져옵니다.
  var inzugElement = document.querySelector(".inzug_btn");

  // 클릭 이벤트를 처리합니다.
  inzugElement.addEventListener("click", function () {
    // "div class="stemp" id="s1"" 요소를 가져옵니다.
    var stempElement = document.querySelector("#s1");

    // 배경 이미지를 변경합니다.
    stempElement.style.backgroundImage = "url('../images/stampO.png')";
    stempElement.style.backgroundSize = "cover";
  });
});

//나의 인증 현황 & 참가자 인증 현황 화면 바뀌는 코드
document
  .getElementById("showDiv2Button")
  .addEventListener("click", function () {
    var div1 = document.getElementById("div1");
    var div2 = document.getElementById("div2");
    var showDiv1Button = document.getElementById("showDiv1Button");
    var showDiv2Button = document.getElementById("showDiv2Button");

    div1.style.display = "none";
    div2.style.display = "block";
    showDiv1Button.style.display = "block";
    showDiv2Button.style.display = "none";
  });

document
  .getElementById("showDiv1Button")
  .addEventListener("click", function () {
    var div1 = document.getElementById("div1");
    var div2 = document.getElementById("div2");
    var showDiv1Button = document.getElementById("showDiv1Button");
    var showDiv2Button = document.getElementById("showDiv2Button");

    div1.style.display = "block";
    div2.style.display = "none";
    showDiv1Button.style.display = "none";
    showDiv2Button.style.display = "block";
  });
