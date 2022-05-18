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
        ajax: "./contacts/data",
        
        // dom: 検索フィールド等の各種ウィジェットの配置
        // https://datatables.net/reference/option/dom
        // dom: 'lfrtip',

        // lengthMenu: １ページに表示させる件数のリスト
        // https://datatables.net/reference/option/lengthMenu
        lengthMenu: [[10, 20, 50, -1], [10, 20, 50, "全件"]],
        lengthChange: false,

        // pageLength: pageLengthの初期値
        // https://datatables.net/reference/option/pageLength
        pageLength: 100,

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

        // columnDefs: [
        //         {targets: 0, data: 'id'},
        //         {targets: 1, data: 'incoming'},
        //         {targets: 2, data: 'name'},
        //         {targets: 3, data: 'tel'},
        //         {targets: 4, data: 'hours'},
        //         {targets: 5, data: 'title'},
        //         {targets: 6, data: 'job'},
        //         {targets: 7, data: 'searchwords'},
        //         {targets: 8, data: 'attachments'},
        //       ],

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
                title: "相手",
                // className: "all",
                // visible: false,
                render: function (data) {
                    let result;
                    if (data == "販社") {
                        result = data.replace("販社", '<div class="card badge-info">&nbsp;販社</div>');
                    } else if (data == "顧客") {
                        result = data.replace("顧客", '<div class="card badge-warning">&nbsp;顧客</div>');
                    } else {
                        result = data;
                    }
                    return result;
                },
            },
            {
                // 3列目
                title: "窓口",
                // className: " all",
                className: 'control',
                render: function (data) {
                    let kaigyo = data.replace(/\r?\n/g, '<br>');
                    return kaigyo;
                },
            },
            {
                // 4列目
                title: "TEL",
                // className: " all",
                render: function (data) {
                    let kaigyo = data.replace(/\r?\n/g, '<br>');
                    return kaigyo;
                },

                // googleマップへのリンク
                // http://www.shurey.com/html/googlemaps.html
                // render: function (data, type, row) {
                //     return '<a target="_blank" href="https://maps.google.co.jp/maps?q=' + row[1] + data + '">' + data + '</a>';
                // },
            },
            {
                // 5列目
                title: "時間",
                render: function (data) {
                    let kaigyo = data.replace(/\r?\n/g, '<br>');
                    return kaigyo;
                },
                // ハイパーリンク追加のサンプル
                // render: function (data) {
                //     let telno = data.replace(/\-/g, '');
                //     return '<a href="tel:' + telno + '">' + data + '</a>';
                // },
            },
            {
                // 6列目：業務
                title: "業務",
                render: function (data) {
                    let aaa = '<br>' + data;
                    let kaigyo = aaa.replace(/\r?\n/g, '<br>');
                    return kaigyo;
                },
            },
            {
                // 7列目：詳細
                title: "詳細",
                // 改行コードをbrへ置換で反映する
                render: function (data) {
                    let aaa = '<br>' + data;
                    let kaigyo = aaa.replace(/\r?\n/g, '<br>');
                    return kaigyo;
                },
            },
            {
                // 8列目
                title: "検索ワード",
                visible: false, // これでもサーチ対象のままになる
            },
            {
                // 9列目
                title: "",
                // visible: false, // これでもサーチ対象のままになる
                
                // render: function (data, type, row) { //typeも必要
                //     return '<a href="' +  data+ '" data-toggle="modal" data-target="#exampleModal" data-title=""\
                //     data-sample="">'+ row[10]  +'</a>';
                // },

                // render: function (data, type, row) { //typeも必要
                //     return '<a class="" data-toggle="modal" data-target="#exampleModal" data-title="<b>' + row[10]+'</b>"\
                //     data-sample="">'+ data +'</a>';
                // },
            },

        ],

        // 列の表示非表示ボタン
        // dom: 'Bfrtip',
        // buttons: [
        //     'colvis'
        // ],

        // レスポンシブ部分全て表示
        responsive: {
            details: {
                display: $.fn.dataTable.Responsive.display.childRowImmediate,
                type: 'none',
                target: ''
            }
        },
        
    });


    // server-side利用時は拡張機能の選択(Select)が使えないので、DataTables公式の
    // サンプルコードを元に選択処理を自作する。
    // https://datatables.net/examples/server_side/select_rows.html
    // $('#datatable tbody').on('click', 'tr', function () {

    //     let id = $(this).attr('data-id');
    //     let index = $.inArray(id, selected);

    //     if (index === -1) {

    //         selected.push(id);
    //         selected.sort(function (a, b) {
    //             return a - b
    //         });
    //         $(this).addClass('selected');
    //     } else {
    //         selected.splice(index, 1);
    //         $(this).removeClass('selected');
    //     }
    //     $('#selected').html(selected.join(','));
    // });

    // サンプル：クリックしたレコードのデータを取得
    // data()でセル、行、表示中のテーブル全体のデータを取得可能
    // https://datatables.net/reference/api/row().data()

    // $('#datatable tbody').on('click', 'tr', function () {
    //     console.log(table.row(this).data());
    // });

    // 全選択を解除
    // $('#clear').on('click', function () {
    //     selected = [];
    //     $('#datatable tr').removeClass('selected');
    //     $('#selected').html(selected.join(','))
    // })

});