# Django用户管理系统

#### 介绍
基于Django框架开发的企业级用户管理系统，集成了用户管理、部门管理、任务管理、订单管理、数据统计等核心功能模块。系统采用前后端分离的设计理念，提供完整的CRUD操作、数据可视化、文件上传等功能。

#### 软件架构
```
mysite/
├── app/                    # 主应用
│   ├── models.py          # 数据模型
│   ├── views/             # 视图层
│   │   ├── user.py        # 用户管理
│   │   ├── depart.py      # 部门管理
│   │   ├── task.py        # 任务管理
│   │   ├── order.py       # 订单管理
│   │   ├── chart.py       # 数据统计
│   │   └── ...
│   ├── templates/         # 模板文件
│   ├── static/            # 静态资源
│   ├── utils/             # 工具组件
│   └── middleware/         # 中间件
├── mysite/                # 项目配置
│   ├── settings.py        # 项目设置
│   ├── urls.py           # URL路由
│   └── ...
└── media/                 # 媒体文件
```

**核心功能模块：**
- 用户管理：用户CRUD、权限控制
- 部门管理：部门信息维护
- 靓号管理：手机号码资源管理
- 任务管理：任务分配与跟踪
- 订单管理：订单处理流程
- 数据统计：图表展示与分析
- 文件管理：图片上传与管理

#### 安装教程

1. **环境准备**
   ```bash
   # 安装Python 3.8+
   # 安装MySQL 5.7+
   # 安装pip
   ```

2. **项目部署**
   ```bash
   # 克隆项目
   git clone [项目地址]
   cd mysite
   
   # 安装依赖
   pip install django==3.2.9
   pip install mysqlclient
   
   # 创建数据库
   mysql -u root -p
   CREATE DATABASE django_final CHARACTER SET utf8mb4;
   ```

3. **配置数据库**
   ```python
   # 修改 mysite/settings.py 中的数据库配置
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'django_final',
           'USER': 'root',
           'PASSWORD': 'your_password',
           'HOST': '127.0.0.1',
           'PORT': 3306,
       }
   }
   ```

4. **初始化项目**
   ```bash
   # 执行数据库迁移
   python manage.py makemigrations
   python manage.py migrate
   
   # 创建超级用户
   python manage.py createsuperuser
   
   # 启动开发服务器
   python manage.py runserver
   ```

#### 使用说明

1. **系统访问**
   - 访问地址：http://127.0.0.1:8000
   - 默认登录页面：http://127.0.0.1:8000/login/

2. **功能使用**
   - **用户管理**：添加、编辑、删除用户信息，支持部门关联
   - **部门管理**：维护组织架构，支持批量操作
   - **任务管理**：创建任务，分配负责人，支持Ajax提交
   - **订单管理**：处理订单流程，状态跟踪
   - **数据统计**：查看柱状图、饼图、折线图等数据可视化
   - **文件上传**：支持图片上传和管理

3. **权限控制**
   - 系统采用中间件进行登录验证
   - 未登录用户自动跳转到登录页面
   - 支持会话管理和用户状态保持

#### 特技

1. **自定义组件**
   - 自定义分页组件，支持灵活配置
   - Bootstrap表单组件，统一UI风格
   - 中间件认证系统，安全可靠

2. **数据可视化**
   - 集成ECharts图表库
   - 支持Highcharts高级图表
   - 实时数据统计和展示

3. **Ajax交互**
   - 无刷新数据提交
   - 异步表单验证
   - 动态内容更新

4. **文件管理**
   - 支持多种文件格式上传
   - 媒体文件统一管理
   - 图片预览和删除功能

5. **响应式设计**
   - Bootstrap响应式布局
   - 移动端友好界面
   - 跨浏览器兼容

6. **代码规范**
   - Django最佳实践
   - 模块化设计
   - 可扩展架构
