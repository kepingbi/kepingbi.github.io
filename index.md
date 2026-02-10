---
title: Home
nav:
  order: 1
---



{% capture left_panel %}

{%- assign image = "/images/profile.jpg" | default: "" -%}
<div class="home-left">
  <div class="home-card">
    <div class="home-portrait">
      <img src="{{ image | relative_url }}" alt="Keping Bi" />
    </div>
    <h1 class="home-name">Keping Bi <span>毕可平</span></h1>
    <div class="home-title">
      Associate Professor<br/>
      Institute of Computing Technology (ICT)<br/>
      Chinese Academy of Sciences (CAS)
    </div>
    <div class="home-address">
      NO. 6 Kexueyuan South Road<br/>
      Haidian District, Beijing, 100190
    </div>
    <div class="home-links">
      {%- include link.html type="google-scholar" icon="" text="Google Scholar" tooltip="" link="kJQYiFIAAAAJ" style="button" -%}
      {%- include link.html type="github" icon="" text="Personal Github" tooltip="" link="KepingBi" style="button" -%}
      {%- include link.html type="twitter" icon="" text="Twitter" tooltip="" link="BiKeping" style="button" -%}
      {%- include link.html type="linkedin" icon="" text="Linkedin" tooltip="" link="keping-bi-b62a3437" style="button" -%}
      {%- include link.html type="email" icon="" text="Email" tooltip="" link="bikeping@ict.ac.cn" style="button" -%}
      {%- include link.html type="home-page" icon="" text="Our Group Homepage" tooltip="" link="https://stay-hungry-time.github.io/" style="button" -%}
      {%- include link.html type="github" icon="" text="Our Group Github" tooltip="" link="Trustworthy-Information-Access" style="button" -%}
      {%- include link.html type="gongzhonghao" icon="" text="Our Group WeChat" tooltip="" link="K7heOgMI04VMAblsGtKusA" style="button" -%}
    </div>
  </div>
</div>

{% endcapture %}

{% capture main_panel %}

<div class="home-right">
  <div class="home-intro">
    <p><strong>Keping Bi</strong>, Associate Professor at Institute of Computing Technology (ICT), Chinese Academy of Sciences (CAS).</p>
    <p>My research centers on <strong><a href="https://stay-hungry-time.github.io/">Trustworthy Information Access</a></strong>, aiming to advance information access systems that are not only effective, but also reliable, transparent, and aligned with human values. As large language models increasingly mediate how people search for, consume, and act on information, I investigate how LLM-based information access systems can be designed to behave honestly, helpfully, and harmlessly, while operating responsibly within the broader information ecosystem.</p>
    <p>My work spans information retrieval, retrieval-augmented generation, agentic search, and model robustness, with a particular focus on understanding and mitigating implicit bias and source bias.</p>
    <p>I earned my Ph.D. from the College of Information and Computer Sciences at the University of Massachusetts (UMass) Amherst, under the guidance of Professor <a href="http://ciir.cs.umass.edu/croft">W. Bruce Croft</a> at the <a href="http://ciir.cs.umass.edu/">Center for Intelligent Information Retrieval (CIIR)</a>. I also hold two master's degrees—one in computer science from UMass Amherst and another in machine intelligence from Peking University—and a bachelor's degree in Computer Science from Nankai University.</p>
    <p><a href="{{ '/experience/' | relative_url }}">See experience and academic services.</a></p>

  </div>

  <div class="home-section">
    <div class="home-section-title">Recruiting</div>
    <p>I'm recruiting self-motivated master students who are interested in conducting innovative research. Undergraduate students who are willing to pursue a Ph.D. or master degree in Institute of Computing Technology CAS or abroad are welcome to do internships in our group. If you are interested, please send your resume to my email address (bikeping[at]ict.ac.cn) and include your research interests and your future plan.</p>
  </div>

  <div class="home-section">
    <div class="home-section-title">Honors & Awards</div>
    <ul class="home-grid">
      <li>ICT Outstanding Researcher, 2025.</li>
      <li>National Young Talent, 2023.</li>
      <li>New Hundred Stars Talent Program, ICT (top 4), 2022.</li>
      <li>Travel Grants: SIGIR'21 Student Travel Grant; WWW'21 Student Scholarship; SIGIR'20 Student Travel Grant; CIKM'19 Student Travel Grant; ECIR'19 Student Travel Grant; SIGIR'18 Travel Grant.</li>
      <li>Baidu Highest Award Nomination (top 10/180+, $1 million reward for teams of 10- members), 2014.</li>
    </ul>
  </div>

  <div class="home-section">
    <div class="home-section-title">News</div>
    <ul class="home-list">
      <li><strong>Jan. 2026</strong>: I will serve as a PC co-chair of ICTIR 2026. </li>
      <li><strong>Jan. 2026</strong>: 2 papers accepted by ICLR 2026. Congrats to Shiyu and Da!</li>
      <li><strong>Dec. 2025</strong>: <a href="https://shiyunee.github.io/">Shiyu</a> has been selected for the Young Elite Scientists Sponsorship Program (Doctoral Students Track), China Association for Science and Technology. Congrats!</li>
      <li><strong>Dec. 2025</strong>: SIGIR-AP 2025 has successfully concluded in Xi'an, and I summarized the event in this <a href="https://mp.weixin.qq.com/s/vq3A4cxLHKEA0TVX16WX9Q">article</a>.</li>
      <li><strong>Nov. 2025</strong>: I gave a keynote talk in the <a href="https://mmgensr-cikm25.github.io/">International Workshop on Multimodal Generative Search and Recommendation in CIKM 2025</a>. The slides can be found on our group website <a href="https://stay-hungry-time.github.io/resources">Smarter Retrieval for Smarter Generation--When and How to Retrieve for Retrieval-Augmented Generation</a>.</li>
      <li><strong>Oct. 2025</strong>: I will serve as a <a href="https://sigir.org/forum/editorial-policy-and-forum-editors/">SIGIR Forum Co-Editor</a> for a three-year term.</li>
      <li><strong>Oct. 2025</strong>: 2 students I supervised got national scholarship (Hengran and Lulu). Congrats!</li>
      <li><strong>Oct. 2025</strong>: 1 paper accepted by WSDM 2026.</li>
      <li><strong>Sep. 2025</strong>: 2 papers accepted by SIGIR-AP 2025.</li>
      <li><strong>Aug. 2025</strong>: 1 paper accepted by CIKM 2025.</li>
      <li><strong>Aug. 2025</strong>: 3 papers accepted by EMNLP 2025 (2 main, 1 findings).</li>
      <li><strong>May 2025</strong>: 2 papers accepted to ACL 2025 (1 main, 1 findings).</li>
      <li><strong>Mar. 2025</strong>: I am serving as a tutorial co-chair of <a href="http://tcci.ccf.org.cn/conference/2025/">NLPCC 2025</a>.</li>
      <li><strong>Feb. 2025</strong>: I am serving as a general co-chair of <a href="https://www.sigir-ap.org/sigir-ap-2025">SIGIR-AP 2025</a>. Welcome your submissions!</li>
    </ul>
  </div>
</div>
<!-- - Promoted Twice at Baidu, 2013, 2014 -->
<!-- - Tencent Campus Practice Competition, Third Prize (top 10%), 2010 -->
<!-- - Outstanding Student Leader of Nankai University (top 5%, 3 times) -->
<!-- - TEDA-Motorola Scholarship (top 10%, gave a speech as a student representative), 2007 -->

<!--**Academic Services**
- [SIGIR](https://sigir.org/general-information/officers-and-volunteers/) Forum Co-Editor
- [SIGIR-AP 2025](https://www.sigir-ap.org/sigir-ap-2025) General Co-chair
- [NLPCC 2025](http://tcci.ccf.org.cn/conference/2025/) Tutorial Co-chair
- [SIGIR-AP 2023](https://www.sigir-ap.org/sigir-ap-2023) Registration Chair

 - Area Chair
  - Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING), 2024
  - ACL Rolling Review (ARR) 2025 (Oct.), 2026 (Jan.)

- PC member / Reviewer:
  - International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR), (short) 2022, (long&short) 2023, (long) 2025, (long) 2026
  - ACL Rolling Review (ARR) 2024 (Feb., June, Oct.), 2025 (Feb., May)
  - The International Conference on Learning Representations, 2026
  - European Conference on Information Retrieval (ECIR), (long) 2026
  - ACM International Conference on Web Search and Data Mining (WSDM), (short) 2026
  - ACM SIGIR Information Retrieval in the Asia Pacific (SIGIR-AP) workshop proposal committee, 2025
  - ACM Web Conference (formerly known as International World Wide Web Conference, WWW), (long) 2025
  - ACM International Conference on Information and Knowledge Management (CIKM), (short) 2020, (short&long)2021, (long)2022, (long&short) 2023, (long&short) 2024, (long) 2025
  - WSDM Workshop on Deep Matching in Practical Applications (DAPA), 2019
  - International Conference on Computer Science and Application Engineering (CSAE), 2019

- Journal Reviewer
  - ACM Transactions on Information Systems (TOIS), 2019, 2020, 2021, 2025
  - International Journal of Data Science and Analytics (IJDSA), 2025
  - Transactions on Intelligent Systems and Technology (TIST), 2023
  - Data & Knowledge Engineering (DKE) 2022
  - Journal of the Association for Information Science and Technology (JASIST), 2020
  - IEEE Access, 2019 -->

{% endcapture %}

<div class="home">
  {% include two-col.html leftcol=left_panel rightcol=main_panel left=3 right=9 %}
</div>
