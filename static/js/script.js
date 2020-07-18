"use strict";

function _createForOfIteratorHelper(o) { if (typeof Symbol === "undefined" || o[Symbol.iterator] == null) { if (Array.isArray(o) || (o = _unsupportedIterableToArray(o))) { var i = 0; var F = function F() {}; return { s: F, n: function n() { if (i >= o.length) return { done: true }; return { done: false, value: o[i++] }; }, e: function e(_e) { throw _e; }, f: F }; } throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); } var it, normalCompletion = true, didErr = false, err; return { s: function s() { it = o[Symbol.iterator](); }, n: function n() { var step = it.next(); normalCompletion = step.done; return step; }, e: function e(_e2) { didErr = true; err = _e2; }, f: function f() { try { if (!normalCompletion && it["return"] != null) it["return"](); } finally { if (didErr) throw err; } } }; }

function _unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === "string") return _arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === "Object" && o.constructor) n = o.constructor.name; if (n === "Map" || n === "Set") return Array.from(o); if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen); }

function _arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) { arr2[i] = arr[i]; } return arr2; }

var checkClick = 0;
var advancedSearchBtn = document.querySelector(".advanced-search-btn");
advancedSearchBtn.addEventListener("click", function () {
  checkClick++;
  advancedSearchClick();
});

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
  }
} //----------------slider-----------------------------


$('.slider').slick({
  infinite: false,
  slidesToShow: 3,
  slidesToScroll: 3,
  variableWidth: true,
  prevArrow: $('.arrow__left'),
  nextArrow: $('.arrow__right')
}); //-----------------блок-предложений-------------------

var hearts = document.querySelectorAll(".heart svg");

var _iterator = _createForOfIteratorHelper(hearts),
    _step;

try {
  var _loop = function _loop() {
    var heart = _step.value;
    var active = false;
    heart.addEventListener("click", function () {
      active = onHeartClick(heart, active);
    });
  };

  for (_iterator.s(); !(_step = _iterator.n()).done;) {
    _loop();
  }
} catch (err) {
  _iterator.e(err);
} finally {
  _iterator.f();
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

var _iterator2 = _createForOfIteratorHelper(numbers),
    _step2;

try {
  var _loop2 = function _loop2() {
    var number = _step2.value;
    number.addEventListener("click", function () {
      number.querySelector(".hidden").classList.remove("hidden");
      number.querySelector(".visible").classList.add("hidden");
    });
  };

  for (_iterator2.s(); !(_step2 = _iterator2.n()).done;) {
    _loop2();
  }
} catch (err) {
  _iterator2.e(err);
} finally {
  _iterator2.f();
}

$('.selectric').selectric();
var $selectValue = $('#select_value').find('strong'); // Get initial value

$selectValue.text($('#get_value').val()); // Initialize Selectric and bind to 'change' event

$('#get_value').selectric().on('change', function () {
  $selectValue.text($(this).val());
});
$('.select').selectric();
var $selectValue = $('#select_value').find('strong'); // Get initial value

$selectValue.text($('#get_value').val()); // Initialize Selectric and bind to 'change' event

$('#get_value').selectric().on('change', function () {
  $selectValue.text($(this).val());
});