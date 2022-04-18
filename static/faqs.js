$(document).ready(function () {

    // 選択中のレコードid
    let selected = [];

    // DataTables 設定
    // https://datatables.net/reference/index
    let table = $('#datatable').DataTable({

        // scrollX: true,
        // autoWidth: false,
        // Server-side processing:Ajaxモードの設定
        // https://datatables.net/examples/server_side/simple.html
        processing: true,
        serverSide: true,
        ajax: "/myinfo/faq2/data", // JsonView.as_view()のURLを書く

        
        // dom: 検索フィールド等の各種ウィジェットの配置
        // https://datatables.net/reference/option/dom
        // dom: 'lfrtip',

        // lengthMenu: １ページに表示させる件数のリスト
        // https://datatables.net/reference/option/lengthMenu
        lengthMenu: [[10, 20, 50, -1], [10, 20, 50, "全件"]],
        lengthChange: false,

        // pageLength: pageLengthの初期値
        // https://datatables.net/reference/option/pageLength
        pageLength: 50,

        // language: 表示メッセージのローカライズ
        // https://datatables.net/reference/option/language
        // 日本語版ソース:https://github.com/DataTables/Plugins/blob/master/i18n/Japanese.lang
        language: {
            "thousands": ",",
            "sProcessing": "処理中...",
            "sLengthMenu": "_MENU_ 件",
            "sZeroRecords": "データはありません。",
            "sInfo": " _TOTAL_ 件中 _START_ ～ _END_ を表示",
            "sInfoEmpty": "データ無し",
            "sInfoFiltered": "（全 _MAX_ 件より抽出）",
            "sInfoPostFix": "",
            "sSearch": "検索:",
            "sUrl": "",
            "oPaginate": {
                "sFirst": "<<",
                "sPrevious": "<",
                "sNext": ">",
                "sLast": ">>"
            },
        },
        // rowCallback: 行の描画時に追加処理を行いたいときに使う。
        // https://datatables.net/reference/option/rowCallback

        // ページ遷移時に選択済みの行の表示を変更している。
        rowCallback: function (row, data) {
            $(row).attr('data-id', data[0]);
            if ($.inArray(data[0], selected) !== -1) {
                $(row).addClass('selected');
            }
        },

        // columns: 列の設定
        // https://datatables.net/reference/option/columns

        // 列の設定は 'columns' または 'columnDefs' で行う。
        // columns のほうが冗長な記述になるが視認性が良い気がする。

        // BaseDatatableViewのcolumnsの設定順にフィールドが列に割り当てられる。
        // columnsのフィールド数より列数が少ないとエラーになるので注意。

        // columnsと実際の列表示の内容を変更したい場合は以下のオプションで工面するとよい。

        // visible: bool    列の表示/非表示
        // data: number     違う列のデータを表示
        // render: function 関数でデータを加工

        // render内で他の列のデータを使うこともできる。
        // https://datatables.net/manual/data/renderers

        columns: [
            {
                // 1列目(id)
                title: "&nbsp;",
                // className: 'select-checkbox',
                searchable: false,
                visible: false,
                render: function () {
                    return "";
                },
            },
            {
                // 2列目
                title: "Q",
                // className: "all",
                // visible: false,
                render: function (data, type, row) {
                    let kaigyo = data.replace('bbb', '<br>');
                    return kaigyo + "<br><br>" + row[4];
                },
                // render: function (data) {
                //     let kaigyo = data.replace('bbb', '<br>');
                //     return kaigyo;
                // },

            },
            {
                // 3列目
                title: "A1",
                // className: " all",
                // className: 'control',
                render: function (data, type, row) {
                    let kaigyo = data.replace('bbb', '<br>');
                    return kaigyo + "<br><br>" + row[3];
                },
            },
            {
                // 4列目
                title: "A2",
                // className: " all",
                visible: false,
                render: function (data) {
                    let kaigyo = data.replace('bbb', '<br>');
                    return kaigyo;
                },

            },
            {
                // 5列目
                title: "参照",
                // className: " all",
                visible: false,
                render: function (data) {
                    let kaigyo = data.replace('bbb', '<br>');
                    return kaigyo;
                },

            },
        ],

        // 列の表示非表示ボタン
        dom: 'Bfrtip',
        buttons: [
            'colvis'
        ],

        // // レスポンシブ部分全て表示
        // responsive: {
        //     details: {
        //         display: $.fn.dataTable.Responsive.display.childRowImmediate,
        //         type: 'none',
        //         target: ''
        //     }
        // },
        
    });

});