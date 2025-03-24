seo_meta_tags = """
<meta property="og:title" content="{{ obituary.name }}">
<meta property="og:description" content="{{ obituary.content|truncatewords:30 }}">
<meta property="og:url" content="{{ request.build_absolute_uri }}">
<meta property="og:type" content="article">
<meta property="og:image" content="/static/images/default.jpg">