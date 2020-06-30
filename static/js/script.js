"use strict";

function _createForOfIteratorHelper(o) { if (typeof Symbol === "undefined" || o[Symbol.iterator] == null) { if (Array.isArray(o) || (o = _unsupportedIterableToArray(o))) { var i = 0; var F = function F() {}; return { s: F, n: function n() { if (i >= o.length) return { done: true }; return { done: false, value: o[i++] }; }, e: function e(_e) { throw _e; }, f: F }; } throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); } var it, normalCompletion = true, didErr = false, err; return { s: function s() { it = o[Symbol.iterator](); }, n: function n() { var step = it.next(); normalCompletion = step.done; return step; }, e: function e(_e2) { didErr = true; err = _e2; }, f: function f() { try { if (!normalCompletion && it["return"] != null) it["return"](); } finally { if (didErr) throw err; } } }; }

function _unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === "string") return _arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === "Object" && o.constructor) n = o.constructor.name; if (n === "Map" || n === "Set") return Array.from(o); if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen); }

function _arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) { arr2[i] = arr[i]; } return arr2; }

var select = document.querySelectorAll(".select");
var body = document.body;
body.addEventListener("click", function (event) {
  var _iterator = _createForOfIteratorHelper(select),
      _step;

  try {
    for (_iterator.s(); !(_step = _iterator.n()).done;) {
      var item = _step.value;

      if (item != event.target) {
        item.querySelector(".select__nav").style.display = "none";
        item.setAttribute('data-close', 'true');
      }
    }
  } catch (err) {
    _iterator.e(err);
  } finally {
    _iterator.f();
  }
});

var _iterator2 = _createForOfIteratorHelper(select),
    _step2;

try {
  var _loop = function _loop() {
    var item = _step2.value;
    item.addEventListener("click", function (event) {
      onNavbarElement(event, item);
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

function onNavbarElement(tag, item) {
  var close = Boolean(item.dataset.close);

  if (close && tag.target.className == "select") {
    item.querySelector(".select__nav").style.display = "block";
    item.setAttribute('data-close', '');
    console.log(tag.target);
  } else if (tag.target.className == "select") {
    item.querySelector(".select__nav").style.display = "none";
    item.setAttribute('data-close', 'true');
  }

  var option = tag.target;

  if (option.className == 'select__option' && !close) {
    item.firstChild.data = option.innerText;
    item.querySelector(".select__nav").style.display = "none";
    item.setAttribute('data-close', 'true');
  }
}

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

var _iterator3 = _createForOfIteratorHelper(hearts),
    _step3;

try {
  var _loop2 = function _loop2() {
    var heart = _step3.value;
    var active = false;
    heart.addEventListener("click", function () {
      active = onHeartClick(heart, active);
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

var _iterator4 = _createForOfIteratorHelper(numbers),
    _step4;

try {
  var _loop3 = function _loop3() {
    var number = _step4.value;
    number.addEventListener("click", function () {
      number.querySelector(".hidden").classList.remove("hidden");
      number.querySelector(".visible").classList.add("hidden");
    });
  };

  for (_iterator4.s(); !(_step4 = _iterator4.n()).done;) {
    _loop3();
  }
} catch (err) {
  _iterator4.e(err);
} finally {
  _iterator4.f();
}