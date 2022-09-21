$(function() {
  function getResult(image) {
    let returnStrA = `分類：`;
    let returnStrB = `狀態：`;
    let failStr = '';
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

  $('#dropzone').change(function (e) { 
    const files = this.files;

    for(let i=0;i<files.length;i++){
      img_file = files[i];

      const fr = new FileReader();
      fr.readAsDataURL(img_file);
  
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
    }
    
  });
});