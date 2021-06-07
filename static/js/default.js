function toggleMode(){
  var mtt = document.querySelector("#mtt");
  var mti = document.querySelector("#mti");
  if (mtt.innerText.match(/DARK MODE/))
  {
    mtt.innerText = "LIGHT MODE";
    mti.classList.replace("fa-moon", 'fa-sun')
    document.documentElement.style.setProperty('--body-bg', "#101012")
    document.documentElement.style.setProperty('--body-fg', "#aaf")
    document.documentElement.style.setProperty('--nav-fg', "rgb(115, 183, 255)")
    document.documentElement.style.setProperty('--nav-bg', "rgb(0, 20, 20)")
    document.documentElement.style.setProperty('--header-fg', "rgb(0, 255, 168)")
    document.documentElement.style.setProperty('--header-bg', "rgb(4, 0, 21)")
    document.documentElement.style.setProperty('--input-fg', "#fff")
    document.documentElement.style.setProperty('--input-bg', "#012")
  }
  else
  {
    mtt.innerText = "DARK MODE";
    mti.classList.replace("fa-sun", 'fa-moon')
    document.documentElement.style.setProperty('--body-fg', "#000")
    document.documentElement.style.setProperty('--body-bg', "#aaa7")
    document.documentElement.style.setProperty('--nav-bg', "rgb(115, 183, 255)")
    document.documentElement.style.setProperty('--nav-fg', "rgb(0, 16, 16)")
    document.documentElement.style.setProperty('--header-bg', "rgb(0, 255, 168)")
    document.documentElement.style.setProperty('--header-fg', "rgb(4, 0, 11)")
    document.documentElement.style.setProperty('--input-fg', "black")
    document.documentElement.style.setProperty('--input-bg', "white")
  }
}


function getUserIp()
{
  var x = [];
  $.getJSON(
    "https://api.ipify.org?format=json",
    function(data) {
      x.push(data.ip);
      console.log(data.ip);
  })
  return x;
}


$(document).ready(function()
{
  $("#mt").click(toggleMode);
})