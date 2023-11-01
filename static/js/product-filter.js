
$(document).ready(function () {
    $(".filter-checkbox").on('click', function () {
        let _filterObj = {};
        $(".filter-checkbox").each(function (index, ele) {
            let _filterVal = $(this).val();
            let _filterKey = $(this).data('filter');
            console.log(_filterKey, _filterVal)
        })
    })
})