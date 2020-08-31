"use strict";

function _createForOfIteratorHelper(o) { if (typeof Symbol === "undefined" || o[Symbol.iterator] == null) { if (Array.isArray(o) || (o = _unsupportedIterableToArray(o))) { var i = 0; var F = function F() {}; return { s: F, n: function n() { if (i >= o.length) return { done: true }; return { done: false, value: o[i++] }; }, e: function e(_e) { throw _e; }, f: F }; } throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); } var it, normalCompletion = true, didErr = false, err; return { s: function s() { it = o[Symbol.iterator](); }, n: function n() { var step = it.next(); normalCompletion = step.done; return step; }, e: function e(_e2) { didErr = true; err = _e2; }, f: function f() { try { if (!normalCompletion && it["return"] != null) it["return"](); } finally { if (didErr) throw err; } } }; }

function _unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === "string") return _arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === "Object" && o.constructor) n = o.constructor.name; if (n === "Map" || n === "Set") return Array.from(o); if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen); }

function _arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) { arr2[i] = arr[i]; } return arr2; }

var checkClick = 0;
var advancedSearchBtn = document.querySelector(".advanced-search-btn");
var showMap = document.querySelector(".show-map");
var advancedBlocks = document.querySelectorAll(".advertisement__block");
var mapGoogle = document.querySelector(".map-google");

if (showMap != null) {
  showMap.addEventListener("click", function () {
    var _iterator = _createForOfIteratorHelper(advancedBlocks),
        _step;

    try {
      for (_iterator.s(); !(_step = _iterator.n()).done;) {
        var block = _step.value;
        block.style.display = "none";
        mapGoogle.style.display = "block";
      }
    } catch (err) {
      _iterator.e(err);
    } finally {
      _iterator.f();
    }
  });
}

if (advancedSearchBtn != null) {
  advancedSearchBtn.addEventListener("click", function () {
    checkClick++;
    advancedSearchClick();
  });
}

function advancedSearchClick() {
  var advancedSearch = document.querySelector(".advanced-search");
  var arrowUp = document.querySelector(".advanced-search-btn .arrow-up");
  var arrowDown = document.querySelector(".advanced-search-btn .arrow-down");

  if (checkClick == 1) {
    document.querySelector(".advanced-search-wrap").style.display = 'block';
    setTimeout(function () {
      return advancedSearch.classList.add("advanced-search_visible");
    }, 100);
    arrowUp.style.display = 'inline-block';
    arrowDown.style.display = 'none';

    if (document.documentElement.clientWidth <= 340) {
      var advertisement = document.querySelector(".advertisement");
      advertisement.style.marginTop = "700px";
    } else if (document.documentElement.clientWidth <= 360) {
      var _advertisement = document.querySelector(".advertisement");

      _advertisement.style.marginTop = "670px";
    } else if (document.documentElement.clientWidth <= 650) {
      var _advertisement2 = document.querySelector(".advertisement");

      _advertisement2.style.marginTop = "640px";
    }
  } else {
    checkClick = 0;
    setTimeout(function () {
      return advancedSearch.classList.remove("advanced-search_visible");
    }, 100);
    setTimeout(function () {
      return document.querySelector(".advanced-search-wrap").style.display = 'none';
    }, 500);
    arrowDown.style.display = 'inline-block';
    arrowUp.style.display = 'none';

    if (document.documentElement.clientWidth <= 340) {
      var _advertisement3 = document.querySelector(".advertisement");

      _advertisement3.style.marginTop = "120px";
    } else if (document.documentElement.clientWidth <= 650) {
      var _advertisement4 = document.querySelector(".advertisement");

      _advertisement4.style.marginTop = "124px";
    }
  }
} //----------------slider-----------------------------


$('.slider').slick({
  infinite: false,
  slidesToShow: 3,
  slidesToScroll: 1,
  variableWidth: true,
  prevArrow: $('.arrow__left'),
  nextArrow: $('.arrow__right'),
  responsive: [{
    breakpoint: 500,
    settings: {
      slidesToShow: 1,
      slidesToScroll: 1
    }
  }]
}); //-----------------блок-предложений-------------------

var hearts = document.querySelectorAll(".heart svg");

var _iterator2 = _createForOfIteratorHelper(hearts),
    _step2;

try {
  var _loop = function _loop() {
    var heart = _step2.value;
    var active = false;
    heart.addEventListener("click", function () {
      active = onHeartClick(heart, active);
    });
  };

  for (_iterator2.s(); !(_step2 = _iterator2.n()).done;) {
    _loop();
  }
} catch (err) {
  _iterator2.e(err);
} finally {
  _iterator2.f();
}

function onHeartClick(heart, active) {
  if (!active) {
    heart.classList.add("heart-active");
    return true;
  } else {
    heart.classList.remove("heart-active");
    return false;
  }
}

var numbers = document.querySelectorAll(".phone-number__block");

var _iterator3 = _createForOfIteratorHelper(numbers),
    _step3;

try {
  var _loop2 = function _loop2() {
    var number = _step3.value;
    number.addEventListener("click", function () {
      number.querySelector(".hidden").classList.remove("hidden");
      number.querySelector(".visible").classList.add("hidden");
    });
  };

  for (_iterator3.s(); !(_step3 = _iterator3.n()).done;) {
    _loop2();
  }
} catch (err) {
  _iterator3.e(err);
} finally {
  _iterator3.f();
}

if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|BB|PlayBook|IEMobile|Windows Phone|Kindle|Silk|Opera Mini/i.test(navigator.userAgent)) {
  $('.selectric').selectric({
    openOnHover: false,
    disableOnMobile: false,
    nativeOnMobile: false
  });
} else {
  $('.selectric').selectric({
    openOnHover: true
  });
}

var $selectValue = $('#select_value').find('strong'); // Get initial value

$selectValue.text($('#get_value').val()); // Initialize Selectric and bind to 'change' event

$('#get_value').selectric().on('change', function () {
  $selectValue.text($(this).val());
});
$('.select').selectric({
  disableOnMobile: false,
  nativeOnMobile: false
});
var $selectValue = $('#select_value').find('strong'); // Get initial value

$selectValue.text($('#get_value').val()); // Initialize Selectric and bind to 'change' event

$('#get_value').selectric().on('change', function () {
  $selectValue.text($(this).val());
}); //----------------------hamburger----------------------

var hamb = document.querySelector(".hamburger");
var nav = document.querySelector(".aside-wrap");
var aside = document.querySelector(".aside");
var delNav = document.querySelector(".x");
var asideStyles = aside.classList;
var navStyles = nav.classList;
hamb.addEventListener("click", function () {
  var _iterator4 = _createForOfIteratorHelper(asideStyles),
      _step4;

  try {
    for (_iterator4.s(); !(_step4 = _iterator4.n()).done;) {
      var style = _step4.value;

      if (style == "aside-out") {
        asideStyles.remove("aside-out");
        asideStyles.add("aside-visible");
      }
    }
  } catch (err) {
    _iterator4.e(err);
  } finally {
    _iterator4.f();
  }

  var _iterator5 = _createForOfIteratorHelper(navStyles),
      _step5;

  try {
    for (_iterator5.s(); !(_step5 = _iterator5.n()).done;) {
      var _style = _step5.value;

      if (_style == "aside-hidden") {
        navStyles.remove("aside-hidden");
        navStyles.add("aside-active");
      }
    }
  } catch (err) {
    _iterator5.e(err);
  } finally {
    _iterator5.f();
  }
});
delNav.addEventListener("click", function () {
  var _iterator6 = _createForOfIteratorHelper(asideStyles),
      _step6;

  try {
    for (_iterator6.s(); !(_step6 = _iterator6.n()).done;) {
      var style = _step6.value;

      if (style == "aside-visible") {
        asideStyles.add("aside-out");
        asideStyles.remove("aside-visible");
      }
    }
  } catch (err) {
    _iterator6.e(err);
  } finally {
    _iterator6.f();
  }

  var _iterator7 = _createForOfIteratorHelper(navStyles),
      _step7;

  try {
    for (_iterator7.s(); !(_step7 = _iterator7.n()).done;) {
      var _style2 = _step7.value;

      if (_style2 == "aside-active") {
        navStyles.remove("aside-active");
        setTimeout(function () {
          return navStyles.add("aside-hidden");
        }, 500);
      }
    }
  } catch (err) {
    _iterator7.e(err);
  } finally {
    _iterator7.f();
  }
});
nav.addEventListener("click", function (event) {
  if (event.target == nav) {
    var _iterator8 = _createForOfIteratorHelper(asideStyles),
        _step8;

    try {
      for (_iterator8.s(); !(_step8 = _iterator8.n()).done;) {
        var style = _step8.value;

        if (style == "aside-visible") {
          asideStyles.add("aside-out");
          asideStyles.remove("aside-visible");
        }
      }
    } catch (err) {
      _iterator8.e(err);
    } finally {
      _iterator8.f();
    }

    var _iterator9 = _createForOfIteratorHelper(navStyles),
        _step9;

    try {
      for (_iterator9.s(); !(_step9 = _iterator9.n()).done;) {
        var _style3 = _step9.value;

        if (_style3 == "aside-active") {
          navStyles.remove("aside-active");
          setTimeout(function () {
            return navStyles.add("aside-hidden");
          }, 500);
        }
      }
    } catch (err) {
      _iterator9.e(err);
    } finally {
      _iterator9.f();
    }
  }
});
/** ----------------Закрытие окна заявки --------------- */

var close = document.querySelector(".close");
var windowWrap = document.querySelector(".window-wrap");
var btnsAd = document.querySelectorAll(".header-top-right__button");

var _iterator10 = _createForOfIteratorHelper(btnsAd),
    _step10;

try {
  for (_iterator10.s(); !(_step10 = _iterator10.n()).done;) {
    var btn = _step10.value;
    btn.addEventListener("click", function () {
      windowWrap.classList.add("window-visible");
      windowWrap.classList.remove("window-hidden");
    });
  }
} catch (err) {
  _iterator10.e(err);
} finally {
  _iterator10.f();
}

close.addEventListener("click", function () {
  windowWrap.classList.add("window-hidden");
  windowWrap.classList.remove("window-visible");
});
windowWrap.addEventListener("click", function (event) {
  if (event.target == windowWrap) {
    windowWrap.classList.add("window-hidden");
    windowWrap.classList.remove("window-visible");
  }
});