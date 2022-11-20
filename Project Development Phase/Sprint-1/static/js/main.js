function openForm() {
    document.getElementById("myForm").style.display = "block";
    document.getElementById("open-btn").style.display = "none";
    document.getElementById("center").style.display = "flex";
    document.getElementById("default").click();
  }
  
  function closeForm() {
    document.getElementById("myForm").style.display = "none";
    document.getElementById("open-btn").style.display = "block";
    document.getElementById("center").style.display = "none";
  }
  function openCity(evt, cityName) {
    // Declare all variables
    var i, tabcontent, tablinks;
  
    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("form-container");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
  
    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
  
    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
  } 
