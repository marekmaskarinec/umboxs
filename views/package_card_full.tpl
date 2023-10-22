<div class="package_card_full box">
        <div>
                <h3><a href="/package/{{p.get('name')}}">{{p.get('name')}} {{p.get('version')}}</a></h3>
                
                <p>{{p.get('description')}}</p>
        </div>
        
        <div>
                <ul>
                        <li><a href="{{p.get('link')}}">Homepage</a></li>
                        <li>License: {{p.get('license')}}</li>
                        <li>Author: {{p.get('author')}}</li>
        </div>
</div>