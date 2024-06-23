document.addEventListener('DOMContentLoaded', function() {
    const description = document.createElement('meta');
    description.name = 'description';
    description.content = 'CenterMold is a professional manufacturer of precision plastic molds offering comprehensive services including mold design, customization, injection molding, CNC parts processing, and assembly. Established in 2006, we are committed to providing high-quality and reliable mold solutions.';
    document.getElementsByTagName('head')[0].appendChild(description);

    const keywords = document.createElement('meta');
    keywords.name = 'keywords';
    keywords.content = 'precision plastic molds, mold design, mold customization, injection molding, CNC parts processing, manufacturing, Shenzhen Shengteng Plastic Mould, high-quality molds, reliable mold solutions, injection mold, mold assembly';
    document.getElementsByTagName('head')[0].appendChild(keywords);

    const author = document.createElement('meta');
    author.name = 'author';
    author.content = 'CenterMold';
    document.getElementsByTagName('head')[0].appendChild(author);

    const robots = document.createElement('meta');
    robots.name = 'robots';
    robots.content = 'index, follow';
    document.getElementsByTagName('head')[0].appendChild(robots);
});
