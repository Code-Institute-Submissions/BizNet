
// -- For card info box to collaps. From Bootstraps -- //
var collapseElementList = [].slice.call(document.querySelectorAll('.collapse'))
var collapseList = collapseElementList.map(function (collapseEl) {
  return new bootstrap.Collapse(collapseEl)
})

$(function () {
  $('[data-toggle="popover-term"]'), poopover()
})

/*
// -- Popover function -- //
var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
  return new bootstrap.Popover(popoverTriggerEl)
})
var popover = new bootstrap.Popover(document.querySelector('[data-bs-toggle="popover"]'), {
  container: 'body'
})
*/

// -- For tabs from Bootstraps -- //
function activaTab(tab) {
  $('.nav-tabs a[href="#' + tab + '"]').tab('show');
};



// -- Activate welcome message -- //

console.log('Welcome!')
console.log(document)

const test = document.getElementById('test')
// const gigs2 = document.getElementById('gigs2')
console.log(test)
/*
setTimeout(() => {
  test.textContent = "Check out the lastest updates below."
}, 2000)
*/
// -- Fetch json for gigs  -- //

$.ajax( {
  type: 'GET',
  url: '/gigs-json/',
  success: function (response) {
    console.log(response.data);
    const data = JSON.parse(response.data);
    console.log(data);
    data.forEach(el => {
      gigs2.innerHTML += `${el.fields.updated}`;
    });
  },
  error: function (error) {
    console.log(error);
  }
});






// -- To call the json data for industry --//
/*
var industryChoice = {
  id: fields._id_prof, 
  industry_name: fields.industry_name,
};


$.ajax({
  type: 'POST',
  url: 'profileusers/fixtures/industry.json',
  contentType: 'application/json; charset=utf-8',
  data: $.toJSON(industryChoice),
  dataType: 'text',
  success: function (result) {
    alert(result.Result);
  }
});
*/