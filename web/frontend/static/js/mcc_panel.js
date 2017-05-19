/**
 * Created by olegas13 on 13.05.17.
 */

/*
 * Store number of panel to hide
 * @type {number}
 */
const NUMBER_VISIBLE_PANEL = 11;

/*
 * This function hide panel
 *
 * @param {object} li panel you want to hide
 *
 * @return {undefined}
 */
function hidePanel(li) {
    li.classList.remove('visible');
    li.classList.add('hidden');
}

/*
 * This function make the panel visible
 *
 * @param {object} li panel you want to visible
 *
 * @return {undefined}
 */
function visiblePanel(li) {
    li.classList.remove('hidden');
    li.classList.add('visible');
}

/*
 * This function find duplicate panel and change their width
 *
 * @return {undefined}
 */
function findDuplicateParameters() {
    // Find all panel without title panel
    let listLi = document.querySelectorAll('ul.param_data > li:nth-child(n+2)');
    for(let i = 0; i < listLi.length; i++) {
        // Get them headers
        let panel_name = listLi[i]
                .querySelectorAll('div:first-child')[0]
                .textContent;
        // If headers contain the numbers, then change panel size
        if(/[0-9]/i.test(panel_name)) {
            // Add class
            listLi[i].classList.add('minPanel');
            // Find round and move him
            listLi[i].querySelectorAll('div:nth-child(2)')[0]
                .classList
                .add('minRound');
        }
    }
}

// Change checkbox processing
$(".check_panel").change(function(){
    let list = document.querySelectorAll(`ul.param_data > li:nth-child(n+${ NUMBER_VISIBLE_PANEL })`);
    for(let i = 0; i < list.length; i++) {
        if(!this.checked)  {
            hidePanel(list[i]);
        } else {
            visiblePanel(list[i]);
        }
    }
});

$('document').ready(function () {
    let listHideLi = document.querySelectorAll(`ul.param_data > li:nth-child(n+${ NUMBER_VISIBLE_PANEL })`);
    // Hide panel when document load
    for(let i = 0; i < listHideLi.length; i++) {
        hidePanel(listHideLi[i]);
    }
    // and find and change size duplicated panels
    findDuplicateParameters();
});


function change_color(name, status) {
    var rou = document.getElementById('s'+name);
    if(status=="ok") {
	rou.classList.add('green_color');
    } 
	else {
	rou.classList.add('red_color');
    }
}
