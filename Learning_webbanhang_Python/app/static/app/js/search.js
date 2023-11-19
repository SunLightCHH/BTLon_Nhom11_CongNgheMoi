function performSearch() {
    // Lấy giá trị từ ô input
    var searchQuery = document.getElementById('search-input').value;
    console.log(searchQuery);
    // Kiểm tra và chuyển hướng tùy thuộc vào giá trị tìm kiếm
    if (searchQuery.toLowerCase() === 'Khổ qua'.toLowerCase()) {
        var bitter_groundUrl = document.getElementById('bitter_groundLink').querySelector('a').getAttribute('href');
        window.location.href = bitter_groundUrl;
    } else if (searchQuery.toLowerCase() === 'Đậu hà lan'.toLowerCase()) {
        var beanUrl = document.getElementById('beanLink').querySelector('a').getAttribute('href');
        window.location.href = beanUrl;
    } else if (searchQuery.toLowerCase() === 'Bầu'.toLowerCase()) {
        var bottle_gourdUrl = document.getElementById('bottle_gourdLink').querySelector('a').getAttribute('href');
        window.location.href = bottle_gourdUrl;
    } else if (searchQuery.toLowerCase() === 'Bông cải xanh'.toLowerCase()) {
        var broccoliUrl = document.getElementById('broccoliLink').querySelector('a').getAttribute('href');
        window.location.href = broccoliUrl;
    } else if (searchQuery.toLowerCase() === 'Bắp cải'.toLowerCase()) {
        var cabbageUrl = document.getElementById('cabbageLink').querySelector('a').getAttribute('href');
        window.location.href = cabbageUrl;
    } else if (searchQuery.toLowerCase() === 'Ớt chuông'.toLowerCase()) {
        var capsicumUrl = document.getElementById('capsicumLink').querySelector('a').getAttribute('href');
        window.location.href = capsicumUrl;
    } else if (searchQuery.toLowerCase() === 'Cà rốt'.toLowerCase()) {
        var carrotUrl = document.getElementById('carrotLink').querySelector('a').getAttribute('href');
        console.log(carrotUrl);
        window.location.href = carrotUrl;
    } else if (searchQuery.toLowerCase() === 'Súp lơ'.toLowerCase()) {
        var cauliflowerUrl = document.getElementById('cauliflowerLink').querySelector('a').getAttribute('href');
        window.location.href = cauliflowerUrl;
    } else if (searchQuery.toLowerCase() === 'Dưa chuột'.toLowerCase()) {
        var cucumberUrl = document.getElementById('cucumberLink').querySelector('a').getAttribute('href');
        window.location.href = cucumberUrl;
    } else if (searchQuery.toLowerCase() === 'Đu đủ'.toLowerCase()) {
        var papayaUrl = document.getElementById('papayaLink').querySelector('a').getAttribute('href');
        window.location.href = papayaUrl;
    } else if (searchQuery.toLowerCase() === 'Khoai tây'.toLowerCase()) {
        var potatoUrl = document.getElementById('potatoLink').querySelector('a').getAttribute('href');
        window.location.href = potatoUrl;
    } else if (searchQuery.toLowerCase() === 'Bí ngô'.toLowerCase()) {
        var pumpkinUrl = document.getElementById('pumpkinLink').querySelector('a').getAttribute('href');
        window.location.href = pumpkinUrl;
    } else if (searchQuery.toLowerCase() === 'Củ cải'.toLowerCase()) {
        var radishUrl = document.getElementById('radishLink').querySelector('a').getAttribute('href');
        window.location.href = radishUrl;
    } else if (searchQuery.toLowerCase() === 'Cà chua'.toLowerCase()) {
        var tomatoUrl = document.getElementById('tomatoLink').querySelector('a').getAttribute('href');
        window.location.href = tomatoUrl;
    }
    else {
        window.location.href = "/search_results/?q=" + encodeURIComponent(searchQuery);
    }
    console.log(window.location.href);
}