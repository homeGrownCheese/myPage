function displayId(element){
  console.log(element.id);
}

function setDate(){
  document.getElementById('date').innerHTML=Date();
}

function showEnglish(element){
  document.getElementById('japanese').innerHTML = "Shane Hoffman";
}

function showJapanese(element){
  document.getElementById('japanese').innerHTML = "シェーン　ホフマン";
}





function setMod(){
  let text = document.lastModified;
  document.getElementById("mod").innerHTML = text;
}





 // const date = new Date(document.lastModified);
 // document.getElementById('mod').innerHTML = date;

