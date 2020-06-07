# wikifortune

<br/>
Note: may not work with some terminals/computers that do not accept unicode.

<br/>

Fix: remove 

      '&\amp;': '&',
      
      '&\copy;': '©',
      
      '&\trade;':'™',
      
<br/>
  from script.
  
 <br/> 
  
May return error on articles containing these characters. 
<br/>
<br/>
Fix: add

    .encode('ascii', 'ignore')
    
to output stream and each return value
  
<br/>
<br/>
<br/>

Usage:
<br/>


      $ wikifortune

      {random wikipedia article ['query']['search'][0]['snippet']}
      More: {link to article}

      $
<br/>
<br/>

example:
<br/>

      $ wikifortune

      Yarnkothrips is a genus of thrips in the family Phlaeothripidae. Yarnkothrips kolourus Roskov Y., Ower G., Orrell T., Nicolson D., Bailly N., Kirk P.M....
      More: https://en.wikipedia.org/wiki/Yarnkothrips
<br/>
<br/>
<br/>
example 2:
<br/>
<br/>

      $ wikifortune test deer articledoesnotexist "lambda calculus"

      Test(s) or TEST may refer to: Test (assessment), an assessment intended to measure the respondents' knowledge or other abilities Test (group), a jazz....
      More: https://en.wikipedia.org/wiki/test

      Deer are the hoofed ruminant mammals forming the family Cervidae. The two main groups of deer are the Cervinae, including the muntjac, the elk (wapiti)....
      More: https://en.wikipedia.org/wiki/deer

      Could not find an article with title matching articledoesnotexist.

      Lambda calculus (also written as λ-calculus) is a formal system in mathematical logic for expressing computation based on function abstraction and application....
      More: https://en.wikipedia.org/wiki/lambda_calculus

      $
<br/>
<br/>
To get a random article inside a request for aticles:
<br/><br/>
use:

      wikifortune foo foo _r_ foo
      
      //_r_ requests random article
<br/><br/>
example:
<br/>
<br/>

      wikifortune corydoras _r_ lambda_calculusarea of distribution of the family, except for Panama where Corydoras is not present. Corydoras species are distributed in South America where found east....
      More: https://en.wikipedia.org/wiki/corydoras


      Kriška Vas (pronounced [ˈkɾiːʃka ˈʋaːs]; Slovene: Kriška vas, in older sources also Križna Vas, German: Kreuzdorf) is a village south of Višnja Gora in....
      More: https://en.wikipedia.org/wiki/Kriška_Vas

      Lambda calculus (also written as λ-calculus) is a formal system in mathematical logic for expressing computation based on function abstraction and application....
      More: https://en.wikipedia.org/wiki/lambda_calculus 
      $





