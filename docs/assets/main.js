(function(){
  var h=document.documentElement;
  function setLang(l){h.dataset.lang=l;h.lang=l;try{localStorage.setItem('pa-lang',l)}catch(e){}}
  try{var s=localStorage.getItem('pa-lang');if(s)setLang(s)}catch(e){}
  document.querySelectorAll('.lang button').forEach(function(b){b.addEventListener('click',function(){setLang(b.dataset.set)})});
  var f=document.getElementById('rfq');
  if(f){f.addEventListener('submit',function(e){
    e.preventDefault();
    var lines=[];f.querySelectorAll('input,select,textarea').forEach(function(el){
      var lab=el.closest('label');var name=lab?lab.querySelector('span[lang="en"]').textContent:el.name;
      if(el.value)lines.push(name+': '+el.value);});
    location.href='mailto:'+f.dataset.mailto+'?subject='+encodeURIComponent('Website enquiry — Prime Atosphere')+'&body='+encodeURIComponent(lines.join('\n'));
  });}
})();
