
BOT_NAME = 'real_estate'
SPIDER_MODULES = ['real_estate.spiders']
NEWSPIDER_MODULE = 'real_estate.spiders'
ITEM_PIPELINES = {'real_estate.pipelines.ValidatePipeline':300, 'real_estate.pipelines.RealEstatePipeline': 500,}

#a = 'HIM LAM PH\u00da AN TR\u1ea2 45% (900TR) NH\u1eacN NH\u00c0'
#b = json.dumps(a, ensure_ascii=False)
#print(b)