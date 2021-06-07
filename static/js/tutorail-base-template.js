function createPath() {
  var host = window.location.host;
  var paths = window.location.pathname.replace('/', '').split('/');
  var linknames = [host].concat(paths);
  var p = document.getElementById('page-nav-path');
 	var links = []
 
  for (var item of linknames){
    links.push(
        item.link(window.location.href.split(item)[0] + item)
    )
  }

  p.innerHTML = links.join(" <span class='nav-symbol'> > </span> ");
}
createPath()

document.querySelector('.table-dropper').addEventListener("click", function(e){
  btn = document.querySelector('.table-dropper').classList.toggle('active')
  document.querySelector('.table-of-content').classList.toggle('hidden')
})

document.querySelector('.text-container').addEventListener("click", function(e){
  toc = document.querySelector('.table-of-content');
  if (!toc.classList.contains('hidden')) {
    toc.classList.add('hidden');
    document.querySelector('.table-dropper').classList.toggle('active')
  }
})