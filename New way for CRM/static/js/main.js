VanillaTilt.init(document.querySelector("#card-custom"), {
    startX: 45,
    startY: 45,
    reset: false,
  });
  
  //It also supports NodeList
  VanillaTilt.init(document.querySelectorAll("#card-custom"));