const toggleSwitch = document.querySelector('.theme-switch input[type="checkbox"]');
const currentTheme = localStorage.getItem('theme');

if (currentTheme) {
    document.documentElement.setAttribute('data-theme', currentTheme);
  
    if (currentTheme === 'dark') {
        toggleSwitch.checked = true;
    }
}

function switchTheme(e) {
    if (e.target.checked) {
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark');
    }
    else { 
      document.documentElement.setAttribute('data-theme', 'light');
          localStorage.setItem('theme', 'light');
    }    
}

toggleSwitch.addEventListener('change', switchTheme, false);


var closeTimeout;

function openBar() {
  clearTimeout(closeTimeout);
  $('.emoji-bar').addClass('emoji-bar--open');
}

function closeBar() {
  closeTimeout = setTimeout(function() {
    $('.emoji-bar').removeClass('emoji-bar--open');
  }, 100);
}

$('.emoji-button').mouseenter(openBar);
$('.emoji-bar').mouseleave(closeBar);

$('.emoji-button').click(function() {
  var button = $(this);
  button.addClass('emoji-button--selected');
  setTimeout(function() {
    closeBar();
  }, 400);
  setTimeout(function() {
    button.removeClass('emoji-button--selected');
  }, 600);
});