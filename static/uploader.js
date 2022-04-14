tinymce.init({
    selector: "textarea#id_body",
    language: "ja",
    // height: "700",
    // width: "1300",
    // plugins: "insertdatetime media image preview",
    // toolbar: "undo redo |  bold italic | alignleft alignright aligncenter alignjustify | image media | preview",
    toolbar: [ // ツールバー(2段)
    "undo redo | bold underline forecolor backcolor emoticons removeformat | fontsizeselect formatselect | outdent indent | \
    alignleft aligncenter alignright | numlist bullist | image media insertfile hr link | preview fullscreen code visualblocks searchreplace ",
    ],
    height: "550px",
    menubar: "edit format insert view table help",
    plugins: "visualblocks template searchreplace hr code autosave advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code fullscreen insertdatetime media table paste code help wordcount emoticons",
    // toolbar: "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft "
    // "aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor "
    // "backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | "
    // "fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | "
    // "a11ycheck ltr rtl | showcomments addcomment code",

    // Enterでbr、shift+Enterで<p>
    forced_root_block :false,

    image_title: true,
    image_caption: true,
    automatic_uploads: true,
    image_advtab: true,
    file_picker_types: "image media",

    font_formats:
    "Andale Mono=andale mono,times;" +
    "Arial=arial,helvetica,sans-serif;" +
    "Arial Black=arial black,avant garde;" +
    "Century Gothic='Century Gothic';" +
    "Comic Sans MS=comic sans ms,sans-serif;" +
    "Helvetica=helvetica;" +
    "Impact=impact,chicago;" +
    "Terminal=terminal,monaco;" +
    "Times New Roman=times new roman,times;" +
    "メイリオ=Meiryo;" +
    "ヒラギノ角ゴ='ヒラギノ角ゴ Pro W3','Hiragino Kaku Gothic Pro','ヒラギノ角ゴ ProN W3','Hiragino Kaku Gothic ProN';" +
    "ヒラギノ丸ゴ='ヒラギノ丸ゴ Pro W4','Hiragino Maru Gothic Pro','ヒラギノ丸ゴ ProN W4','Hiragino Maru Gothic ProN';" +
    "ＭＳ Ｐゴシック='ＭＳ Ｐゴシック','MS PGothic';" +
    "ＭＳ ゴシック='ＭＳ ゴシック','MS Gothic';" +
    "游ゴシック='游ゴシック','Yu Gothic';" ,
    // "ヒラギノ明朝='ヒラギノ明朝 Pro W3','Hiragino Mincho Pro',ヒラギノ明朝 ProN W3','Hiragino Mincho ProN';" +
    // "ＭＳ Ｐ明朝='ＭＳ Ｐ明朝','MS PMincho';" +
    // "ＭＳ 明朝='ＭＳ 明朝','MS Mincho';" +
    // "游明朝='游明朝','Yu Mincho';",

    fontsize_formats: "8pt 10pt 11pt 12pt 14pt 18pt 24pt 36pt",
 


    file_picker_callback: function (cb, value, meta) {
      var input = document.createElement("input");
      input.setAttribute("type", "file");
      if (meta.filetype == "image") {
          input.setAttribute("accept", "image/*");}
      if (meta.filetype == "media") {
      input.setAttribute("accept", "video/*");}

      input.onchange = function () {     
          var file = this.files[0];
          var reader = new FileReader();
          reader.onload = function () {
              var id = "blobid" + (new Date()).getTime();
              var blobCache =  tinymce.activeEditor.editorUpload.blobCache;
              var base64 = reader.result.split(",")[1];
              var blobInfo = blobCache.create(id, file, base64);
              blobCache.add(blobInfo);
             cb(blobInfo.blobUri(), { title: file.name });
           };
           reader.readAsDataURL(file);
       };
       input.click();
    },
    content_style: "body { font-family:Helvetica,Arial,sans-serif; font-size:14px }"
});