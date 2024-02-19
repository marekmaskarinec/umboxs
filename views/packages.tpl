% include('header.tpl', title=title)

<h1>{{title}}</h1>

% packages.sort(key=lambda p: p[0])
% for n in packages:
        % include('package_card_full.tpl', p=n[1])
% end

% include('footer.tpl')