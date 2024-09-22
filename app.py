from flask import Flask, render_template, abort

app = Flask(__name__)

# Dummy data
projects = [
    {
        'title': 'Project 1',
        'description': 'Description of project 1',
        'image': 'project1.png'
    },
    {
        'title': 'Project 2',
        'description': 'Description of project 2',
        'image': 'project2.png'
    },
]

# Sample data representing blog posts
blogs = [
    {
        'id': 1,
        'title': 'First Blog Post',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam pulvinar risus non nisi posuere, in accumsan velit convallis. Nulla facilisi. Curabitur quis quam id velit venenatis ultricies. Aliquam auctor, nisl ut tempor feugiat, elit mi fermentum velit, eget lacinia velit arcu in nisl.',
        'author': 'John Doe',
        'date_posted': '2024-07-10',
        'image_url': 'https://via.placeholder.com/800x400'
    },
    {
        'id': 2,
        'title': 'Second Blog Post',
        'content': 'Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Nam varius nisi vel magna tristique lacinia.',
        'author': 'Jane Smith',
        'date_posted': '2024-07-09',
        'image_url': 'https://via.placeholder.com/800x400'
    }
    # Add more blog entries as needed
]

recent_posts = [
    {'id': 1, 'title': 'first Blog Post'},
    {'id': 2, 'title': 'second Blog Post'}
]

categories = ['Category 1', 'Category 2', 'Category 3']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects_page():
    return render_template('projects.html', projects=projects)

@app.route('/blogs')
def blogs_page():
    return render_template('blogs.html', blogs=blogs)

@app.route('/blogs/<int:blog_id>')
def blog_detail(blog_id):
    blog = next((b for b in blogs if b['id'] == blog_id), None)
    if blog is None:
        abort(404)
    return render_template('blog_detail.html', blog=blog,recent_posts=recent_posts, categories=categories)

@app.route('/about_boss')
def about_boss():
    return render_template('about_boss.html')

# if __name__ == '__main__':
#     app.run(debug=True)
