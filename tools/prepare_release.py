#!/usr/bin/env python3
"""TURBINE WEB-01: deterministic SEO metadata + sitemap generator.

Builds an isolated preview (noindex) or an indexable release after founder approval.
Does not publish anything or send tracking data.
"""
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from html import escape
import argparse,json,re,shutil,xml.etree.ElementTree as ET

DEFAULT_BASE='https://access-mark.github.io/TURBINE-BusinessOS-V4-R5-Business-First-Journey-Review/'
TITLE={
 'index.html':'Your Business, Working as One | TURBINE BusinessOS',
 'my-business.html':'A Simpler Working Day for Your Business | TURBINE',
 'why-turbine.html':'Why TURBINE BusinessOS? A Clearer Way to Run Business',
 'capabilities.html':'BusinessOS Capabilities: Customers, Work, Money & Control',
 'occupations.html':'Business Software by Occupation: 780 South African Roles',
 'occupation.html':'Find Your Occupation | TURBINE BusinessOS',
 'business-types.html':'BusinessOS for Sole Proprietors, QSEs, SMEs and Enterprise',
 'industries.html':'BusinessOS by Industry: 16 South African Business Journeys',
 'journeys.html':'Connected Business Workflows: From Enquiry to Payment',
 'getting-started.html':'How to Adopt TURBINE BusinessOS | Guided Starting Point',
 'adoption.html':'Adopt a Complete BusinessOS: Guided Onboarding and Change',
 'experience.html':'See TURBINE Today and Flow | Product Experience Preview',
 'platform.html':'The TURBINE BusinessOS Platform | One Operating Environment',
 'migration.html':'DataPort Import and Export | Move Business Data Safely',
 'guide.html':'TURBINE Guide | Guided Business Navigation and Next Steps',
 'pricing.html':'TURBINE BusinessOS Pricing Approach and Discovery',
 'trial.html':'Request a Qualified TURBINE BusinessOS Trial',
 'contact.html':'Talk to TURBINE | BusinessOS Enquiries and Discovery',
 'security.html':'TURBINE BusinessOS Security, Governance and Trust',
 'command.html':'TURBINE Command | Governed Onboarding and Entitlements',
 'faq.html':'TURBINE BusinessOS FAQ | Pricing, Trials and Data',
 'about.html':'About TURBINE BusinessOS | Built for Connected Business',
 'accessibility.html':'Website Accessibility | TURBINE BusinessOS',
 'privacy.html':'Website Privacy | TURBINE BusinessOS',
 'terms.html':'Website Terms and Product Limitations | TURBINE',
 'solutions.html':'TURBINE BusinessOS Solutions by Industry and Work',
 '404.html':'Page Not Found | TURBINE BusinessOS',
}
DESC={
 'index.html':'Running a business takes enough work. See how TURBINE could help keep customers, work and money connected, whether you work for yourself or lead a team.',
 'my-business.html':'Work for yourself, run a team or lead a larger business? Follow a simple, practical day showing what a connected business could look like.',
 'why-turbine.html':'Why TURBINE? Explore five practical beliefs behind one connected way to manage customers, work, people, decisions and money.',
 'capabilities.html':'Discover how CRM, quotations, scheduling, purchasing, stock, accounting and reporting connect through one practical business journey.',
 'occupations.html':'Search 780 occupations, from gardeners and estate agents to QSE owners and CEOs, and find practical business workflows relevant to your work.',
 'occupation.html':'Search occupations to find relatable business journeys, from first enquiry through delivery and payment, across South African industries.',
 'business-types.html':'Explore how TURBINE fits sole proprietors, microbusinesses, South African QSEs, SMEs, medium firms and enterprise operations.',
 'industries.html':'Explore 16 industry-specific business journeys showing how customers, operations, purchases and cash flow connect in TURBINE BusinessOS.',
 'journeys.html':'Follow real business journeys from a customer enquiry through quotations, work, purchasing, invoicing and management visibility.',
 'getting-started.html':'See how discovery, data preparation, guided adoption and qualified onboarding could help your business move to one connected system.',
 'adoption.html':'Understand the governed adoption route for TURBINE BusinessOS: discovery, data migration, responsibility, validation and a controlled start.',
 'experience.html':'View authentic TURBINE Today and TURBINE Flow development screenshots, and understand what the qualified product experience is designed to provide.',
 'platform.html':'Learn how customers, work, finance, governance and guided decisions are designed to operate together in TURBINE BusinessOS.',
 'migration.html':'Explore DataPort Import and Export Studio: mapping, validation, reconciliation, safe retries and customer data portability.',
 'guide.html':'See the intended guided TURBINE experience: begin with your work, find the next action and retain context across connected workflows.',
 'pricing.html':'Understand TURBINE BusinessOS discovery, commercial qualification and subscription approach without invented prices or hidden checkout.',
 'trial.html':'Explore the governed path to a qualified TURBINE BusinessOS trial. This page is an enquiry, not automatic tenant creation.',
 'contact.html':'Discuss the work your business needs to connect, including discovery, migration, BusinessOS adoption and partnership enquiries.',
 'security.html':'Understand TURBINE security design, identity, tenant isolation, approvals, audit, recovery and independent qualification requirements.',
 'command.html':'Learn how TURBINE Command is intended to govern onboarding, consent, identity, entitlements and commercial operations.',
 'faq.html':'Answers to common questions about TURBINE BusinessOS, trials, accounting, migration, business size and product qualification.',
 'about.html':'Understand the TURBINE BusinessOS mission: make complex business work easier to follow without sacrificing control or accountability.',
 'accessibility.html':'TURBINE website accessibility approach, keyboard navigation and ongoing accessibility qualification.',
 'privacy.html':'Privacy information for the TURBINE BusinessOS website preview and planned qualified services.',
 'terms.html':'Read the TURBINE website terms, product preview limitations and boundaries around trial availability.',
 'solutions.html':'Find connected business journeys for professional services, manufacturing, retail, medical administration and other South African sectors.',
 '404.html':'The page you requested could not be found. Return to the TURBINE BusinessOS home page or browse occupations and industries.',
}
INDUSTRIES={
 1:('Professional Services','Connect client briefs, proposals, work and invoices. Explore how TURBINE could support South African consultants, accountants and practices.'),
 2:('IT Services and Managed Providers','Keep client requests, support delivery, projects, hardware sourcing and recurring commercial commitments connected.'),
 3:('Manufacturing','Connect customer orders to purchasing, production work, inventory, dispatch and cash flow in one manufacturing journey.'),
 4:('Retail and Wholesale','Follow stock purchases, supplier receipts, store sales, inventory exceptions and margin in a connected retail workflow.'),
 5:('Construction and Contracting','Explore how project estimates, variations, site work, subcontractors and staged billing can connect.'),
 6:('Healthcare Administration','Coordinate non-clinical scheduling, teams, suppliers and business finances with appropriate privacy boundaries.'),
 7:('Mining and Industrial Services','Connect industrial work scopes, qualified resources, procurement, completion evidence and commercial follow-up.'),
 8:('Estate Agents and Property Services','Keep buyers, sellers, viewings, maintenance tasks, approvals and financial follow-ups in one working picture.'),
 9:('Education and Training','Coordinate non-academic administration, facilities, purchasing, programmes and accountability for education organisations.'),
 10:('Marketing and Creative Agencies','Follow client briefs, campaign work, revisions, approvals, supplier costs and project billing.'),
 11:('Logistics and Field Services','Connect dispatch commitments, drivers, service exceptions, proof of completion and customer invoicing.'),
 12:('Hospitality and Accommodation','Coordinate bookings, staff schedules, procurement, service delivery and daily financial visibility.'),
 13:('Agriculture and Agribusiness','Follow seasonal plans, agricultural inputs, equipment work, purchasing, delivery commitments and cash.'),
 14:('Repairs and Maintenance','Connect customer callouts, estimates, technicians, parts, job completion and payments.'),
 15:('Sole-Proprietor Practices','Discover how independent professionals can manage enquiries, quotations, schedules and getting paid without admin overload.'),
 16:('Nonprofits and Community Organisations','Track programme commitments, tasks, supplier expenditure, milestones and reporting for nonprofit operations.'),
}

def set_meta(soup, name,content, property=False):
 key='property' if property else 'name'
 tag=soup.head.find('meta',attrs={key:name})
 if not tag:tag=soup.new_tag('meta');tag[key]=name;soup.head.append(tag)
 tag['content']=str(content)

def set_link(soup,rel,href):
 tag=soup.head.find('link',rel=rel)
 if not tag:tag=soup.new_tag('link');tag['rel']=rel;soup.head.append(tag)
 tag['href']=href

def clean_meta(soup):
 for x in soup.head.select('meta[name="robots"],meta[name="keywords"],link[rel="canonical"],meta[property^="og:"],meta[name^="twitter:"],script[type="application/ld+json"]'):
  x.decompose()

def human_title(p,soup):
 if p.name.startswith('industry-'):
  n=int(p.stem.split('-')[1]);return 'BusinessOS for '+INDUSTRIES[n][0]+' | TURBINE'
 if p.parent.name=='roles':
  h=soup.h1.get_text(' ',strip=True).split(':')[0];return 'Business Software for '+h+' | TURBINE BusinessOS'
 return TITLE.get(p.name,soup.title.get_text(' ',strip=True))

def human_desc(p,soup):
 if p.name.startswith('industry-'):
  return INDUSTRIES[int(p.stem.split('-')[1])][1]
 if p.parent.name=='roles':
  lead=soup.select_one('main .page-hero .lead')
  return (lead.get_text(' ',strip=True)+' See five practical steps for connected customer, work and payment decisions.')[:180].rsplit(' ',1)[0]+'.'
 return DESC.get(p.name,'Explore practical connected business journeys in TURBINE BusinessOS.')

def breadcrumbs(relative,soup,base):
 label=soup.h1.get_text(' ',strip=True) if soup.h1 else relative.replace('.html','').replace('-',' ').title()
 if relative=='index.html':return None
 if relative.startswith('roles/'):
  levels=[('Home','index.html'),('Who it is for','occupations.html'),(label,relative)]
 elif relative.startswith('industry-'):
  levels=[('Home','index.html'),('Industries','industries.html'),(label,relative)]
 else:levels=[('Home','index.html'),(label,relative)]
 return {'@type':'BreadcrumbList','itemListElement':[
  {'@type':'ListItem','position':i,'name':name,'item':urljoin(base,href)} for i,(name,href) in enumerate(levels,1)
 ]}

def prepare(source,target,base,mode):
 if mode not in ('preview','release'):raise ValueError('mode')
 if not (base.startswith('https://') and base.endswith('/')):raise ValueError('base-url must be an https:// URL ending in /')
 if source.resolve()!=target.resolve():
  if target.exists():shutil.rmtree(target)
  shutil.copytree(source,target)
 files=sorted(target.glob('*.html'))+sorted((target/'roles').glob('*.html'))
 sitemap_groups={'core':[],'industries':[],'occupations':[]}
 for path in files:
  rel=path.relative_to(target).as_posix()
  soup=BeautifulSoup(path.read_text(),'lxml')
  if not soup.head:raise ValueError('head missing '+rel)
  clean_meta(soup)
  title=human_title(path,soup);description=human_desc(path,soup)
  if not soup.head.title:soup.head.append(soup.new_tag('title'))
  soup.head.title.string=title
  set_meta(soup,'description',description)
  # Preserve preview safety. Dynamic occupation shell is always noindex to
  # avoid a query-string URL explosion and near-duplicate indexed pages.
  if mode=='preview' or rel in ('404.html','occupation.html'):
   set_meta(soup,'robots','noindex, follow')
  else:set_meta(soup,'robots','index, follow, max-image-preview:large')
  canonical=urljoin(base,rel)
  if rel=='occupation.html':canonical=urljoin(base,'occupations.html')
  if rel=='404.html':canonical=urljoin(base,'index.html')
  set_link(soup,'canonical',canonical)
  set_meta(soup,'og:type','website',True)
  set_meta(soup,'og:site_name','TURBINE BusinessOS',True)
  set_meta(soup,'og:locale','en_ZA',True)
  set_meta(soup,'og:title',title,True)
  set_meta(soup,'og:description',description,True)
  set_meta(soup,'og:url',canonical,True)
  set_meta(soup,'og:image',urljoin(base,'assets/today-dark.png'),True)
  set_meta(soup,'og:image:alt','TURBINE Today business operating environment preview',True)
  set_meta(soup,'twitter:card','summary_large_image')
  set_meta(soup,'twitter:title',title)
  set_meta(soup,'twitter:description',description)
  set_meta(soup,'twitter:image',urljoin(base,'assets/today-dark.png'))
  for x in soup.head.select('link[rel="preconnect"]'):x.decompose()
  for url in ['https://fonts.googleapis.com','https://fonts.gstatic.com']:
   t=soup.new_tag('link',rel='preconnect',href=url)
   if 'gstatic' in url:t['crossorigin']='anonymous'
   soup.head.append(t)
  if rel=='index.html':
   # Critical hero image should not wait for lazy loading; set dimensions
   # where known, and allow browser to prioritise its fetch.
   images=soup.select('main .hero img')
   for img in images:
    if 'today-dark.png' in img.get('src',''):
     img.attrs.pop('loading',None);img['fetchpriority']='high';img['decoding']='async'
  graph=[{'@type':'WebPage','@id':canonical+'#webpage','url':canonical,'name':title,'description':description,'inLanguage':'en-ZA','isPartOf':{'@id':urljoin(base,'index.html')+'#website'}}]
  if rel=='index.html':
   graph += [
    {'@type':'WebSite','@id':urljoin(base,'index.html')+'#website','name':'TURBINE BusinessOS','url':base,'inLanguage':'en-ZA','publisher':{'@id':base+'#organization'}},
    {'@type':'Organization','@id':base+'#organization','name':'TURBINE BusinessOS','url':base,'logo':{'@type':'ImageObject','url':urljoin(base,'assets/logo-dark-transparent.png')}}
   ]
  bread=breadcrumbs(rel,soup,base)
  if bread:
   bread['@id']=canonical+'#breadcrumb';graph.append(bread)
  if rel=='occupations.html':
   ids=json.loads((target/'SEO_CURATED_ROLE_IDS.json').read_text())
   graph.append({'@type':'ItemList','name':'Business stories by occupation','itemListElement':[
    {'@type':'ListItem','position':i,'url':urljoin(base,'roles/'+rid+'.html')} for i,rid in enumerate(ids,1)]})
  script=soup.new_tag('script',type='application/ld+json')
  script.string=json.dumps({'@context':'https://schema.org','@graph':graph},ensure_ascii=False,separators=(',',':')).replace('</','<\\/')
  soup.head.append(script)
  path.write_text(str(soup))
  if rel not in ('404.html','occupation.html'):
   group='occupations' if rel.startswith('roles/') else ('industries' if rel.startswith('industry-') else 'core')
   sitemap_groups[group].append(urljoin(base,rel))

 ET.register_namespace('','http://www.sitemaps.org/schemas/sitemap/0.9')
 ns='{http://www.sitemaps.org/schemas/sitemap/0.9}'
 for group,urls in sitemap_groups.items():
  root=ET.Element(ns+'urlset')
  for url in urls:
   node=ET.SubElement(root,ns+'url');ET.SubElement(node,ns+'loc').text=url
   ET.SubElement(node,ns+'lastmod').text='2026-11-16'
  ET.ElementTree(root).write(target/('sitemap-'+group+'.xml'),encoding='utf-8',xml_declaration=True)
 root=ET.Element(ns+'sitemapindex')
 for group in ('core','industries','occupations'):
  node=ET.SubElement(root,ns+'sitemap');ET.SubElement(node,ns+'loc').text=urljoin(base,'sitemap-'+group+'.xml')
  ET.SubElement(node,ns+'lastmod').text='2026-11-16'
 ET.ElementTree(root).write(target/'sitemap.xml',encoding='utf-8',xml_declaration=True)
 (target/'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: '+urljoin(base,'sitemap.xml')+'\n')
 summary={'base_url':base,'mode':mode,'pages':len(files),'indexable_in_release':sum(map(len,sitemap_groups.values())),'sitemaps':{k:len(v) for k,v in sitemap_groups.items()},'note':'Preview is intentionally noindexed. Release-mode build requires founder approval; generation alone is not release acceptance.'}
 (target/'SEO_BUILD_MANIFEST.json').write_text(json.dumps(summary,indent=2))
 print(json.dumps(summary,indent=2))
 return summary

if __name__=='__main__':
 parser=argparse.ArgumentParser()
 parser.add_argument('--source',required=True)
 parser.add_argument('--output',required=True)
 parser.add_argument('--base-url',default=DEFAULT_BASE)
 parser.add_argument('--mode',choices=['preview','release'],default='preview')
 parser.add_argument('--founder-accepted',action='store_true',help='Explicit authorisation required for indexable release-mode output')
 a=parser.parse_args()
 if a.mode=='release' and not a.founder_accepted:
  parser.error('Release mode requires --founder-accepted after closure of launch gates')
 prepare(Path(a.source),Path(a.output),a.base_url,a.mode)
