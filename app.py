from flask import Flask, render_template, send_from_directory, request
import os

app = Flask(__name__)

# 设置静态文件夹路径
@app.route('/template/<path:filename>')
def serve_template(filename):
    return send_from_directory('template', filename)

@app.route('/images/<path:filename>')
def serve_images(filename):
    # 如果您将来会添加图片，它们将被放在images目录下
    return send_from_directory('images', filename)

# 主页路由
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# 预约页面路由
@app.route('/appointment')
def appointment():
    return "预约页面 - 待开发"

# 针对404错误的处理
@app.errorhandler(404)
def page_not_found(e):
    return f"页面未找到 - {e}", 404

if __name__ == '__main__':
    # 检查必要的文件和文件夹是否存在
    if not os.path.exists('index.html'):
        print("警告: index.html文件未找到!")
    
    if not os.path.exists('template'):
        print("警告: template文件夹未找到!")
    else:
        if not os.path.exists('template/style.css'):
            print("警告: template/style.css文件未找到!")
        
    if not os.path.exists('images'):
        print("警告: images文件夹未找到!")
        os.makedirs('images', exist_ok=True)
        
    print("服务器启动中...")
    print("请访问 http://localhost:5000 查看您的网站")
    
    # 启动Flask应用，开启调试模式，允许外部访问
    app.run(debug=True, host='0.0.0.0', port=5000)