import IPython
from IPython.display import HTML


def GameDisplay():
    IPython.display.HTML('''
    <button id='left-btn'>←</button>
    <button id='right-btn'>→</button>
    <button id='up-btn'>↑</button>
    <button id='down-btn'>↓</button>
    <button id='a-btn'>A</button>
    <button id='b-btn'>B</button>
    <div style="height: 3px"></div>
    <script>
    const div = document.createElement('div');
    document.body.appendChild(div);
    const dst_canvas = document.createElement('canvas');
    dst_canvas.width = "720";
    dst_canvas.height = "400";
    const dst_canvasCtx = dst_canvas.getContext('2d');
    div.appendChild(dst_canvas);

    document.querySelector('#left-btn').onclick = () => {
        var send_num = 0
        _canvasUpdate();
        async function _canvasUpdate() {
            if(send_num < 1){
                send_num += 1;
                const results = google.colab.kernel.invokeFunction('notebook.updatadisplay', [1], {});
                results.then(function(value) {
                    parse = JSON.parse(JSON.stringify(value))["data"];
                    parse = JSON.parse(JSON.stringify(parse))["application/json"];
                    parse = JSON.parse(JSON.stringify(parse))["img_str"];
                    var image = new Image();
                    image.src = parse;
                    image.onload = function(){dst_canvasCtx.drawImage(image, 0, 0)};
                    send_num -= 1;
                })
                requestAnimationFrame(_canvasUpdate);
            }
        }
      };

    document.querySelector('#right-btn').onclick = () => {
        var send_num = 0
        _canvasUpdate();
        async function _canvasUpdate() {
            if(send_num < 1){
                send_num += 1;
                const results = google.colab.kernel.invokeFunction('notebook.updatadisplay', [2], {});
                results.then(function(value) {
                    parse = JSON.parse(JSON.stringify(value))["data"];
                    parse = JSON.parse(JSON.stringify(parse))["application/json"];
                    parse = JSON.parse(JSON.stringify(parse))["img_str"];
                    var image = new Image();
                    image.src = parse;
                    image.onload = function(){dst_canvasCtx.drawImage(image, 0, 0)};
                    send_num -= 1;
                })
                requestAnimationFrame(_canvasUpdate);
            }
        }
      };

    document.querySelector('#up-btn').onclick = () => {
        var send_num = 0
        _canvasUpdate();
        async function _canvasUpdate() {
            if(send_num < 1){
                send_num += 1;
                const results = google.colab.kernel.invokeFunction('notebook.updatadisplay', [3], {});
                results.then(function(value) {
                    parse = JSON.parse(JSON.stringify(value))["data"];
                    parse = JSON.parse(JSON.stringify(parse))["application/json"];
                    parse = JSON.parse(JSON.stringify(parse))["img_str"];
                    var image = new Image();
                    image.src = parse;
                    image.onload = function(){dst_canvasCtx.drawImage(image, 0, 0)};
                    send_num -= 1;
                })
                requestAnimationFrame(_canvasUpdate);
            }
        }
      };

    document.querySelector('#down-btn').onclick = () => {
        var send_num = 0
        _canvasUpdate();
        async function _canvasUpdate() {
            if(send_num < 1){
                send_num += 1;
                const results = google.colab.kernel.invokeFunction('notebook.updatadisplay', [4], {});
                results.then(function(value) {
                    parse = JSON.parse(JSON.stringify(value))["data"];
                    parse = JSON.parse(JSON.stringify(parse))["application/json"];
                    parse = JSON.parse(JSON.stringify(parse))["img_str"];
                    var image = new Image();
                    image.src = parse;
                    image.onload = function(){dst_canvasCtx.drawImage(image, 0, 0)};
                    send_num -= 1;
                })
                requestAnimationFrame(_canvasUpdate);
            }
        }
      };

    document.querySelector('#a-btn').onclick = () => {
        var send_num = 0
        _canvasUpdate();
        async function _canvasUpdate() {
            if(send_num < 1){
                send_num += 1;
                const results = google.colab.kernel.invokeFunction('notebook.updatadisplay', [11], {});
                results.then(function(value) {
                    parse = JSON.parse(JSON.stringify(value))["data"];
                    parse = JSON.parse(JSON.stringify(parse))["application/json"];
                    parse = JSON.parse(JSON.stringify(parse))["img_str"];
                    var image = new Image();
                    image.src = parse;
                    image.onload = function(){dst_canvasCtx.drawImage(image, 0, 0)};
                    send_num -= 1;
                })
                requestAnimationFrame(_canvasUpdate);
            }
        }
      };

    document.querySelector('#b-btn').onclick = () => {
        var send_num = 0
        _canvasUpdate();
        async function _canvasUpdate() {
            if(send_num < 1){
                send_num += 1;
                const results = google.colab.kernel.invokeFunction('notebook.updatadisplay', [12], {});
                results.then(function(value) {
                    parse = JSON.parse(JSON.stringify(value))["data"];
                    parse = JSON.parse(JSON.stringify(parse))["application/json"];
                    parse = JSON.parse(JSON.stringify(parse))["img_str"];
                    var image = new Image();
                    image.src = parse;
                    image.onload = function(){dst_canvasCtx.drawImage(image, 0, 0)};
                    send_num -= 1;
                })
                requestAnimationFrame(_canvasUpdate);
            }
        }
      };
    </script>
    ''')
