from flask import Flask
app = Flask(__name__) 

@app.route("/")
def decorator():
    return("""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Currículo — Diego Garcia</title>
  <link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@300;400;500&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet"/>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --bg: #f5f4f1;
      --surface: #ffffff;
      --ink: #1a1a18;
      --muted: #7a7a72;
      --accent: #0a3d62;
      --accent-light: #e8f0f8;
      --border: #e2e1dc;
      --mono: 'DM Mono', monospace;
      --sans: 'DM Sans', sans-serif;
    }

    html { font-size: 15px; }

    body {
      background: var(--bg);
      color: var(--ink);
      font-family: var(--sans);
      font-weight: 300;
      line-height: 1.7;
      min-height: 100vh;
      padding: 3rem 1.5rem;
      -webkit-font-smoothing: antialiased;
    }

    .page {
      max-width: 820px;
      margin: 0 auto;
      background: var(--surface);
      border: 1px solid var(--border);
      padding: 4rem 4.5rem;
      position: relative;
      animation: fadeUp 0.6s ease both;
    }

    @keyframes fadeUp {
      from { opacity: 0; transform: translateY(18px); }
      to   { opacity: 1; transform: translateY(0); }
    }

    /* ─── HEADER ─── */
    .header {
      display: grid;
      grid-template-columns: 1fr auto;
      gap: 2rem;
      align-items: start;
      padding-bottom: 2.5rem;
      border-bottom: 1px solid var(--border);
      margin-bottom: 2.5rem;
    }

    .name {
      font-family: var(--sans);
      font-size: 2.6rem;
      font-weight: 600;
      letter-spacing: -0.04em;
      line-height: 1.1;
      color: var(--ink);
    }

    .title-tag {
      font-family: var(--mono);
      font-size: 0.7rem;
      font-weight: 400;
      color: var(--accent);
      background: var(--accent-light);
      padding: 0.3rem 0.75rem;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      display: inline-block;
      margin-top: 0.75rem;
    }

    .contact-grid {
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
      align-items: flex-end;
      padding-top: 0.25rem;
    }

    .contact-item {
      font-family: var(--mono);
      font-size: 0.72rem;
      color: var(--muted);
      letter-spacing: 0.02em;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .contact-item a {
      color: var(--muted);
      text-decoration: none;
      transition: color 0.2s;
    }

    .contact-item a:hover { color: var(--accent); }

    .dot {
      width: 5px; height: 5px;
      border-radius: 50%;
      background: var(--accent);
      flex-shrink: 0;
    }

    /* ─── SUMMARY ─── */
    .summary {
      font-size: 0.95rem;
      color: var(--muted);
      line-height: 1.8;
      max-width: 600px;
      margin-bottom: 2.5rem;
      padding-bottom: 2.5rem;
      border-bottom: 1px solid var(--border);
    }

    /* ─── SECTION ─── */
    section { margin-bottom: 2.5rem; }

    .section-label {
      font-family: var(--mono);
      font-size: 0.62rem;
      font-weight: 500;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      color: var(--accent);
      margin-bottom: 1.25rem;
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .section-label::after {
      content: '';
      flex: 1;
      height: 1px;
      background: var(--border);
    }

    /* ─── EXPERIENCE ─── */
    .entry {
      display: grid;
      grid-template-columns: 1fr auto;
      gap: 0.25rem 2rem;
      margin-bottom: 1.75rem;
      padding-bottom: 1.75rem;
      border-bottom: 1px solid var(--border);
    }

    .entry:last-child { border-bottom: none; margin-bottom: 0; padding-bottom: 0; }

    .entry-role {
      font-size: 1rem;
      font-weight: 600;
      color: var(--ink);
      letter-spacing: -0.01em;
    }

    .entry-company {
      font-size: 0.85rem;
      color: var(--muted);
      margin-top: 0.1rem;
    }

    .entry-period {
      font-family: var(--mono);
      font-size: 0.68rem;
      color: var(--muted);
      white-space: nowrap;
      padding-top: 0.25rem;
      text-align: right;
    }

    .entry-desc {
      grid-column: 1 / -1;
      font-size: 0.87rem;
      color: var(--muted);
      line-height: 1.75;
      margin-top: 0.5rem;
    }

    .entry-tags {
      grid-column: 1 / -1;
      display: flex;
      flex-wrap: wrap;
      gap: 0.4rem;
      margin-top: 0.65rem;
    }

    .tag {
      font-family: var(--mono);
      font-size: 0.65rem;
      color: var(--accent);
      border: 1px solid var(--accent-light);
      background: var(--accent-light);
      padding: 0.2rem 0.55rem;
      letter-spacing: 0.03em;
    }

    /* ─── SKILLS ─── */
    .skills-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.25rem;
    }

    .skill-group-title {
      font-family: var(--mono);
      font-size: 0.7rem;
      font-weight: 500;
      color: var(--ink);
      letter-spacing: 0.05em;
      margin-bottom: 0.5rem;
    }

    .skill-list {
      list-style: none;
    }

    .skill-list li {
      font-size: 0.82rem;
      color: var(--muted);
      line-height: 1.9;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .skill-list li::before {
      content: '—';
      color: var(--border);
      font-size: 0.7rem;
    }

    /* ─── EDUCATION ─── */
    .edu-entry {
      display: grid;
      grid-template-columns: 1fr auto;
      gap: 0.15rem 2rem;
      margin-bottom: 1.25rem;
    }

    .edu-entry:last-child { margin-bottom: 0; }

    .edu-degree {
      font-size: 0.95rem;
      font-weight: 500;
      color: var(--ink);
    }

    .edu-school {
      font-size: 0.82rem;
      color: var(--muted);
    }

    .edu-year {
      font-family: var(--mono);
      font-size: 0.68rem;
      color: var(--muted);
      text-align: right;
      padding-top: 0.2rem;
    }

    /* ─── FOOTER ─── */
    .footer-line {
      margin-top: 3rem;
      padding-top: 1.5rem;
      border-top: 1px solid var(--border);
      font-family: var(--mono);
      font-size: 0.62rem;
      color: var(--border);
      letter-spacing: 0.1em;
      text-transform: uppercase;
      text-align: center;
    }

    @media (max-width: 640px) {
      .page { padding: 2rem 1.5rem; }
      .header { grid-template-columns: 1fr; }
      .contact-grid { align-items: flex-start; }
      .skills-grid { grid-template-columns: 1fr 1fr; }
      .name { font-size: 2rem; }
    }

    @media print {
      body { background: white; padding: 0; }
      .page { border: none; padding: 2cm; box-shadow: none; }
    }
  </style>
</head>
<body>
<div class="page">

  <!-- HEADER -->
  <header class="header">
    <div>
      <div class="name">Diego Garcia</div>
      <div class="title-tag">Engenheiro de Software Sênior</div>
    </div>
    <div class="contact-grid">
      <div class="contact-item"><span class="dot"></span>Belo Horizonte, MG</div>
      <div class="contact-item"><span class="dot"></span><a href="mailto:joao@email.com">joao@email.com</a></div>
      <div class="contact-item"><span class="dot"></span><a href="tel:+5531900000000">(31) 9 0000-0000</a></div>
      <div class="contact-item"><span class="dot"></span><a href="#">linkedin.com/in/joaosilva</a></div>
      <div class="contact-item"><span class="dot"></span><a href="#">github.com/joaosilva</a></div>
    </div>
  </header>

  <!-- RESUMO -->
  <p class="summary">
    Engenheiro de software com 8 anos de experiência no desenvolvimento de sistemas escaláveis e de alta disponibilidade. 
    Especialista em arquitetura de microsserviços, cloud computing e liderança técnica de times ágeis. 
    Apaixonado por código limpo, boas práticas e entrega de valor real ao produto.
  </p>

  <!-- EXPERIÊNCIA -->
  <section>
    <div class="section-label">Experiência</div>

    <div class="entry">
      <div class="entry-role">Engenheiro de Software Sênior</div>
      <div class="entry-period">2022 — atual</div>
      <div class="entry-company">Nubank · Belo Horizonte, MG</div>
      <div class="entry-desc">
        Liderança técnica de squad responsável pelo sistema de processamento de transações em tempo real, 
        atendendo mais de 5 milhões de requisições diárias. Reduzi a latência média em 40% após 
        reestruturação da camada de cache e otimização de queries no banco de dados distribuído.
      </div>
      <div class="entry-tags">
        <span class="tag">Kotlin</span>
        <span class="tag">Clojure</span>
        <span class="tag">Kafka</span>
        <span class="tag">Datomic</span>
        <span class="tag">AWS</span>
        <span class="tag">Kubernetes</span>
      </div>
    </div>

    <div class="entry">
      <div class="entry-role">Desenvolvedor Full Stack Pleno</div>
      <div class="entry-period">2019 — 2022</div>
      <div class="entry-company">Totvs · Belo Horizonte, MG</div>
      <div class="entry-desc">
        Desenvolvimento e manutenção de módulos financeiros do ERP Protheus, com foco em performance 
        e integração via API REST. Conduzi a migração de serviços legados para arquitetura de microsserviços, 
        reduzindo tempo de deploy em 60%.
      </div>
      <div class="entry-tags">
        <span class="tag">Java</span>
        <span class="tag">Spring Boot</span>
        <span class="tag">React</span>
        <span class="tag">PostgreSQL</span>
        <span class="tag">Docker</span>
      </div>
    </div>

    <div class="entry">
      <div class="entry-role">Desenvolvedor Backend Junior</div>
      <div class="entry-period">2017 — 2019</div>
      <div class="entry-company">Stefanini Group · Belo Horizonte, MG</div>
      <div class="entry-desc">
        Desenvolvimento de APIs RESTful para sistema de gestão de frotas de grande porte. 
        Colaborei na implementação de autenticação OAuth2 e integração com serviços de geolocalização.
      </div>
      <div class="entry-tags">
        <span class="tag">Python</span>
        <span class="tag">Django</span>
        <span class="tag">MySQL</span>
        <span class="tag">Redis</span>
      </div>
    </div>
  </section>

  <!-- HABILIDADES -->
  <section>
    <div class="section-label">Habilidades</div>
    <div class="skills-grid">
      <div>
        <div class="skill-group-title">Linguagens</div>
        <ul class="skill-list">
          <li>Kotlin / Java</li>
          <li>Python</li>
          <li>TypeScript</li>
          <li>Go</li>
          <li>SQL</li>
        </ul>
      </div>
      <div>
        <div class="skill-group-title">Infraestrutura</div>
        <ul class="skill-list">
          <li>AWS / GCP</li>
          <li>Kubernetes</li>
          <li>Docker</li>
          <li>Terraform</li>
          <li>CI/CD</li>
        </ul>
      </div>
      <div>
        <div class="skill-group-title">Práticas & Ferramentas</div>
        <ul class="skill-list">
          <li>Microsserviços</li>
          <li>Event-Driven</li>
          <li>TDD / BDD</li>
          <li>Code Review</li>
          <li>Metodologias Ágeis</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- FORMAÇÃO -->
  <section>
    <div class="section-label">Formação</div>

    <div class="edu-entry">
      <div>
        <div class="edu-degree">MBA em Arquitetura de Software</div>
        <div class="edu-school">FIAP — Faculdade de Informática e Administração Paulista</div>
      </div>
      <div class="edu-year">2021 — 2022</div>
    </div>

    <div class="edu-entry">
      <div>
        <div class="edu-degree">Bacharelado em Ciência da Computação</div>
        <div class="edu-school">UFMG — Universidade Federal de Minas Gerais</div>
      </div>
      <div class="edu-year">2013 — 2017</div>
    </div>
  </section>

  <!-- CERTIFICAÇÕES -->
  <section>
    <div class="section-label">Certificações</div>

    <div class="edu-entry">
      <div>
        <div class="edu-degree">AWS Certified Solutions Architect – Professional</div>
        <div class="edu-school">Amazon Web Services</div>
      </div>
      <div class="edu-year">2023</div>
    </div>

    <div class="edu-entry">
      <div>
        <div class="edu-degree">Certified Kubernetes Administrator (CKA)</div>
        <div class="edu-school">Cloud Native Computing Foundation</div>
      </div>
      <div class="edu-year">2022</div>
    </div>
  </section>

  <div class="footer-line">Atualizado em Maio de 2026 · Disponível para oportunidades presenciais e remotas</div>
</div>
</body>
</html>
""")

if __name__ == "__main__" :
    app.run(debug=True)