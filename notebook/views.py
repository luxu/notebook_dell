from django.shortcuts import render

from selenium import webdriver
from selenium.common.exceptions import (
    NoSuchElementException
)

from notebook.models import Notebook


def index(request):
    template_name = 'index.html'
    notebooks = Notebook.objects.all()
    context = {
        'object_list': notebooks
    }
    return render(request, template_name, context)


def update_notebooks(request):
    template_name = 'update_notebooks.html'
    list_url = [
        'https://www.dell.com/pt-br/shop/notebooks-dell/sr/laptops/intel-core-i7?appliedRefinements=6084'
    ]
    # 'https://deals.dell.com/pt-br/work/category/notebooks?appliedRefinements=201'
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    for url in list_url:
        browser.get(url)
        for box in browser.find_elements_by_tag_name('article'):
            title = box.find_element_by_tag_name('h3').text
            print(title)
        # for box in browser.find_elements_by_class_name('sd-ps-stack')[2:]:
        #     try:
        #         title = box.find_element_by_class_name('sd-ps-title').text
        #         price_orig = box.find_element_by_class_name('sd-ps-orig').text.split('De ')[1]
        #         price_dell = box.find_element_by_class_name('sd-ps-dell-price').text.split('\n')[1]
        #         discount = box.find_element_by_class_name('sd-ps-sav').text.split('Desconto ')[1]
        #         freight = box.find_element_by_class_name('sd-ps-del').text.split('Frete ')[1]
        #         especs = box.find_elements_by_class_name('sd-ps-spec-item')
        #         name_proc = especs[0].text
        #         name_so = especs[1].text
        #         name_video_card = especs[2].text
        #         name_monitor = especs[3].text
        #         name_ssd = especs[4].text
        #         name_ram = especs[5].text
        #         description = box.find_element_by_class_name('sd-ps-short-desc').text.split('\n')[0]
        #         notebook = Notebook(
        #             title=title,
        #             price_orig=price_orig,
        #             price_dell=price_dell,
        #             discount=discount,
        #             freight=freight,
        #             name_proc=name_proc,
        #             name_so=name_so,
        #             name_video_card=name_video_card,
        #             name_monitor=name_monitor,
        #             name_ssd=name_ssd,
        #             name_ram=name_ram,
        #             description=description,
        #         )
        #         notebook.save()
        #         print(f'Salvo!! {title}')
        #     except NoSuchElementException:
        #         break
        #     break
        browser.quit()
    return render(request, template_name)
