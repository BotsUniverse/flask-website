function createAudio(data)
{
  try{
    // document.querySelector('p').innerText = 'http://127.0.0.1:7000/'+data
    var audio = new Audio;
    audio.src = window.location.origin + "/" + data;
    console.log(audio.src)
    audio.controls = true;
    document.querySelector('.audios').append(audio)
    document.querySelector('.loading').remove()
  }
  catch(err)
  {
    console.log(err)
    setTimeout(function()
    {
      createAudio(data);
    }, 1000) 
  }
}
function getAudio(path) {
  $.ajax({
    type: "GET",
    url: window.location.origin + '/' + path,
    data: {},
    success: function(data) {
      createAudio(path);
    },
    error: function(data) {
      setTimeout(
        function(){ getAudio(path) },
        2000
      )
    }
  })
}


$(document).ready(function(){
  console.log('TTS SCRIPT CONNECTED!')


  // the audio fetcher
  $('#button').click(e=>{
    const text = $("#text").val();
    const p = document.querySelector('.audios');
    var loader = document.createElement('div');
    loader.className="loading"
    p.append(loader)
    $.ajax({
      type: 'POST',
      url:   window.location.origin + '/fetch/tts',
      data: {
        "text": text,
        "gender": "male",
        "speechrate": "none"
      },
      success: function (data){
        console.log(data)
        getAudio(data)
      }
    })
  })



})