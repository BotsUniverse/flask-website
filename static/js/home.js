function arrangeTabs()
{
  // select all the containers
  var containers = document.querySelectorAll('.card-container');
  containers.forEach(
    (e, n)=>
    {
      var class_list = e.classList;
      // eliminate the current tab
      if ( !class_list.contains('active') )
      {
        // move the tab to make other tab visible 
        e.children[0].children[0].style.left = `calc(${n} * 120px)`
      }
      else
      {
        e.children[0].style.transform = `translateX(0px)`
      }
    }
  )
}


function switchTab(){

  var active = document.querySelector(".card-container.active");

  var tab = this;
  var card = this.parentNode;
  var container = card.parentNode;
  
  active.classList.remove('active');
  container.classList.add('active');
  card.style.transform = `translateX(0px)`
  arrangeTabs()
}


function nextBtn(){
  console.log('Next Button Clicked')
  var containers = document.querySelectorAll('.card-container');
  var done = false
  containers.forEach(
    (e, n) => {
      var classlist = e.classList;
      if (classlist.contains('active') && !done)
      {
        console.log('switch active active')
        e.classList.remove('active');
        containers[(n+1)%containers.length].classList.add('active');
        console.log(n%containers.length)
        done= true;
        arrangeTabs();
      }
    }
  )
}


// assembel the parts
$(document).ready(function()
{
  arrangeTabs();
  $('.tab').click(switchTab);
  $('.next-btn').click(nextBtn);
  $('.domain-origin').text(window.location.origin)
})