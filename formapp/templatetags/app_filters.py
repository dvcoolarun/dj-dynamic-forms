# /templatetags/app_filters.py
from django import template
register = template.Library()

# get specific list from querydict
# Use : querydict | get_list {{ querydict|get_list:"list_to_get"}}

@register.filter
def get_list(querydict, list_to_get):

    list_name = list_to_get + '_list'

    list_name = []

    if list_to_get == 'mssa_question':
        for idx, item in enumerate(querydict['mssa_question']):
            list_name.append([querydict['mssa_question'][idx], querydict['mssa_option1'][idx], querydict[
                             'mssa_option2'][idx], querydict['mssa_option3'][idx], querydict['mssa_option4'][idx]])

    elif list_to_get == 'msma_question':
        for idx, item in enumerate(querydict['msma_question']):
            list_name.append([querydict['msma_question'][idx], querydict['msma_option1'][idx], querydict[
                'msma_option2'][idx], querydict['msma_option3'][idx], querydict['msma_option4'][idx]])

    elif list_to_get == 'paragraph_question':
        for idx, item in enumerate(querydict['paragraph_question']):
            list_name.append([querydict['paragraph_question'][
                             idx], querydict['paragraph_text'][idx]])

    elif list_to_get == 'boolean_question':
        for idx, item in enumerate(querydict['boolean_question']):
            list_name.append([querydict['boolean_question'][idx]])


    return list_name
