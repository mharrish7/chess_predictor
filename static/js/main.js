console.log("linked");

$('#imgPreview').hide();
$('.spinner-border').hide();
$("#form").on("submit",function(e){
  $('.spinner-border').fadeIn();
    formdata = new FormData($("#form")[0]);
    $.ajax({
        data :formdata,
        type : 'POST',
        url : '/pred',
        contentType: false,
        cache: false,
        processData: false
    })
    .done(function(data) {
      if(data.error){
        $('#res').text(data['error'])
      }
      else{
        $('#res').text(data['data'])
      }
    });
    $('.spinner-border').fadeOut();
    e.preventDefault();
});


$('#file').change(function(){
  $('#imgPreview').hide();
  
    const file = this.files[0];
    if (file){
      let reader = new FileReader();
      reader.onload = function(event){
        $('#imgPreview').attr('src', event.target.result);
      }
      reader.readAsDataURL(file);
    }
    $('#imgPreview').fadeIn();
  });
