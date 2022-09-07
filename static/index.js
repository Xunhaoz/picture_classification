(function init() {
  const dropzone = document.getElementById("dropzone");
  function getResult(image) {
    var returnStrA = `分類：`;
    var returnStrB = `狀態：`;
    var failStr = '';
    $.ajax({
      async:false,
      type: "post",
      url: "/",
      data: {
        contentType: false,
        processData: false,
        data: image
      },
      success: function (response) {
        returnStrA += response['class_name'];
        returnStrB += response['status'];
        failStr += response['reason'];
      }
    });

    if (failStr != 'undefined'){alert(failStr)}
    return returnStrA + '<br>' + returnStrB;
  }

  dropzone.addEventListener("change", function () {
    
    const file = this.files[0];
    const fr = new FileReader();
    fr.readAsDataURL(file);

    fr.addEventListener("load", function () {
      const resultMsg =  getResult(fr.result);
      resultBlock = `<div class="col"><div class="card">
      <img src="${fr.result}"  class="card-img-top" alt="imgError">
        <div class="card-body">
          <h5 >${resultMsg}</h5>
        </div>
      </div></div>`;
      $("#resultBlock").prepend(resultBlock);
    });
  });
})();

