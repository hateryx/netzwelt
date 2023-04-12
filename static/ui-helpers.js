const toggler = document.getElementById("territories");

toggler.addEventListener("click", (event) => {
  const element = event.target.id;
  const parentChecker = element.split("-");
  console.log(element);

  if (parentChecker[0] == "parent" || parentChecker[0] == "carat") {
    const childFinder = "child" + "-" + parentChecker[1];
    const childFound = document.getElementById(childFinder);

    const caratFinder = "carat" + "-" + parentChecker[1];
    const caratFound = document.getElementById(caratFinder);

    if (caratFound) {
      if (caratFound.classList.contains("rotate-180")) {
        caratFound.classList.remove("rotate-180");
        caratFound.classList.add("rotate-90");
      } else {
        caratFound.classList.remove("rotate-90");
        caratFound.classList.add("rotate-180");
      }
    }

    if (childFound) {
      if (childFound.classList.contains("hidden")) {
        childFound.classList.remove("hidden");
        console.log(element, childFinder);
      } else {
        childFound.classList.add("hidden");
      }
    }
  }
});
