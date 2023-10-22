% include('header.tpl', title=title)

<h1>{{title}}</h1>

% for n in packages:
        % include('package_card_full.tpl', p=n[1])
% end

% include('footer.tpl')