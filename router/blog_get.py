from typing import Optional
from fastapi import APIRouter, status, Response
from enum import Enum

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


# Colocar 1ro /blog/all para resolver antes que /blog/:id
# @app.get('/blog/all')
# def get_all_blogs():
#     return {'message': 'All Blogs provided'}

@router.get(
    '/all',
    summary='Retrieve all blogs',
    description='This api call simulates fetching all blogs.',
    response_description='List of available blogs'
    )
# def get_all_blogs(default param, optional param)
def get_all_blogs(page = 1, page_size: Optional[int] = None):
    return {'message': f'All { page_size } blogs on page { page }'}

# Example path & query params
@router.get('/{id}/comments/{comment_id}', tags=['comment'])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    """
    Simulates retrieving a comment of a blog
    
    - **id** mandatory path parameter
    - **comment_id** mandatory path parameter
    - **valid** optional query parameter
    - **username** optional query parameter    
    """
    
    return {'message': f'blog_id { id }, comment_id { comment_id }, valid { valid }, username { username }'}

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'
    
@router.get('/type/{type}')
# usar Enum forza a que se acepte solo sus atributos de BlogType
def get_blog_type(type: BlogType):
    return {'message': f'Blog type {type}'}
    
@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'Blog with id {id}'}


