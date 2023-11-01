$(document).ready(function () {
    // код начинает работать, только когда весь шаблон загружен
    $('.ajaxLoader').hide()
    let originalProductsHTML = $('#filteredProducts').html() // общий список продуктов
    $('.filter-checkbox').on('click', function () {
        let _filterObj = {}
        $('.filter-checkbox').each(function (index, ele) {
            // выбирает все элементы с указанным классом и выполняет функцию к каждому
            let _filterVal = $(this).val() // получает значение текущего чекбокса
            let _filterKey = $(this).data('filter') // получает значение атрибута data-filter текущего чекбокса
            _filterObj[_filterKey] = Array.from(document.querySelectorAll('input[data-filter=' + _filterKey + ']:checked')).map(function (el) {
                return el.value
            }) // Array.from делает из псевдомассива массив, map извлекает значение value  из каждого чекбокса и возвращает в новом массиве
        })
        let filterActive = Object.values(_filterObj).some((arr) => arr.length > 0) // проверяет, есть ли хотя бы один параметр фильтра, у которого выбраны какие-либо значения

        if (filterActive) {
            // Выполнять AJAX-запрос только если есть активные фильтры
            performAjaxRequest(_filterObj)
        } else {
            // Восстановить исходные товары
            $('#filteredProducts').html(originalProductsHTML)
        }

        // AJAX
        function performAjaxRequest(_filterObj) {
            let subcategory_pk = window.location.pathname.split('/').pop() // получаем из урла первичный ключ подкатегории
            $.ajax({
                url: '/filter-data/' + subcategory_pk,
                data: _filterObj,
                dataType: 'json',
                beforeSend: function () {
                    $('.ajaxLoader').show()
                },
                success: function (res) {
                    let filteredProductsHTML = $(res.data).find('#filteredProducts').html() // получает данные из data и потом берет нужное из элементов с указаным id
                    $('#filteredProducts').html(filteredProductsHTML)
                    $('.ajaxLoader').hide()
                }
            })
        }
    })
})