import pandas as pd

query = """
  WITH 
dicionario_capital AS (
    SELECT
        chave AS chave_capital,
        valor AS descricao_capital
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'capital'
        AND id_tabela = 'microdados'
),
dicionario_v1022 AS (
    SELECT
        chave AS chave_v1022,
        valor AS descricao_v1022
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'v1022'
        AND id_tabela = 'microdados'
),
dicionario_a003 AS (
    SELECT
        chave AS chave_a003,
        valor AS descricao_a003
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'a003'
        AND id_tabela = 'microdados'
),
dicionario_a005 AS (
    SELECT
        chave AS chave_a005,
        valor AS descricao_a005
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'a005'
        AND id_tabela = 'microdados'
),
dicionario_b0011 AS (
    SELECT
        chave AS chave_b0011,
        valor AS descricao_b0011
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'b0011'
        AND id_tabela = 'microdados'
),
dicionario_b0012 AS (
    SELECT
        chave AS chave_b0012,
        valor AS descricao_b0012
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'b0012'
        AND id_tabela = 'microdados'
),
dicionario_b0013 AS (
    SELECT
        chave AS chave_b0013,
        valor AS descricao_b0013
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'b0013'
        AND id_tabela = 'microdados'
),
dicionario_b0015 AS (
    SELECT
        chave AS chave_b0015,
        valor AS descricao_b0015
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'b0015'
        AND id_tabela = 'microdados'
),
dicionario_b00111 AS (
    SELECT
        chave AS chave_b00111,
        valor AS descricao_b00111
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'b00111'
        AND id_tabela = 'microdados'
),
dicionario_b002 AS (
    SELECT
        chave AS chave_b002,
        valor AS descricao_b002
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'b002'
        AND id_tabela = 'microdados'
),
dicionario_b0033 AS (
    SELECT
        chave AS chave_b0033,
        valor AS descricao_b0033
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'b0033'
        AND id_tabela = 'microdados'
),
dicionario_b0034 AS (
    SELECT
        chave AS chave_b0034,
        valor AS descricao_b0034
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'b0034'
        AND id_tabela = 'microdados'
),
dicionario_b0035 AS (
    SELECT
        chave AS chave_b0035,
        valor AS descricao_b0035
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'b0035'
        AND id_tabela = 'microdados'
),
dicionario_b005 AS (
    SELECT
        chave AS chave_b005,
        valor AS descricao_b005
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'b005'
        AND id_tabela = 'microdados'
),
dicionario_b006 AS (
    SELECT
        chave AS chave_b006,
        valor AS descricao_b006
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'b006'
        AND id_tabela = 'microdados'
),
dicionario_b007 AS (
    SELECT
        chave AS chave_b007,
        valor AS descricao_b007
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'b007'
        AND id_tabela = 'microdados'
),
dicionario_b009a AS (
    SELECT
        chave AS chave_b009a,
        valor AS descricao_b009a
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'b009a'
        AND id_tabela = 'microdados'
),
dicionario_b009b AS (
    SELECT
        chave AS chave_b009b,
        valor AS descricao_b009b
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'b009b'
        AND id_tabela = 'microdados'
),
dicionario_c001 AS (
    SELECT
        chave AS chave_c001,
        valor AS descricao_c001
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'c001'
        AND id_tabela = 'microdados'
),
dicionario_c002 AS (
    SELECT
        chave AS chave_c002,
        valor AS descricao_c002
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'c002'
        AND id_tabela = 'microdados'
),
dicionario_c003 AS (
    SELECT
        chave AS chave_c003,
        valor AS descricao_c003
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'c003'
        AND id_tabela = 'microdados'
),
dicionario_c005 AS (
    SELECT
        chave AS chave_c005,
        valor AS descricao_c005
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'c005'
        AND id_tabela = 'microdados'
),
dicionario_c007c AS (
    SELECT
        chave AS chave_c007c,
        valor AS descricao_c007c
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'c007c'
        AND id_tabela = 'microdados'
),
dicionario_c01011 AS (
    SELECT
        chave AS chave_c01011,
        valor AS descricao_c01011
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'c01011'
        AND id_tabela = 'microdados'
),
dicionario_c013 AS (
    SELECT
        chave AS chave_c013,
        valor AS descricao_c013
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'c013'
        AND id_tabela = 'microdados'
),
dicionario_f001 AS (
    SELECT
        chave AS chave_f001,
        valor AS descricao_f001
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'f001'
        AND id_tabela = 'microdados'
),
dicionario_f0022 AS (
    SELECT
        chave AS chave_f0022,
        valor AS descricao_f0022
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'f0022'
        AND id_tabela = 'microdados'
)
SELECT
    dados.ano as ano,
    dados.mes as mes,
    dados.semana as semana,
    dados.sigla_uf AS sigla_uf,
    diretorio_sigla_uf.nome AS sigla_uf_nome,
    descricao_capital AS capital,
    descricao_v1022 AS v1022,
    dados.a002 as a002,
    descricao_a003 AS a003,
    descricao_a005 AS a005,
    descricao_b0011 AS b0011,
    descricao_b0012 AS b0012,
    descricao_b0013 AS b0013,
    descricao_b0015 AS b0015,
    descricao_b00111 AS b00111,
    descricao_b002 AS b002,
    descricao_b0033 AS b0033,
    descricao_b0034 AS b0034,
    descricao_b0035 AS b0035,
    descricao_b005 AS b005,
    descricao_b006 AS b006,
    descricao_b007 AS b007,
    descricao_b009a AS b009a,
    descricao_b009b AS b009b,
    descricao_c001 AS c001,
    descricao_c002 AS c002,
    descricao_c003 AS c003,
    descricao_c005 AS c005,
    descricao_c007c AS c007c,
    descricao_c01011 AS c01011,
    descricao_c013 AS c013,
    descricao_f001 AS f001,
    descricao_f0022 AS f0022
FROM `basedosdados.br_ibge_pnad_covid.microdados` AS dados
LEFT JOIN (SELECT DISTINCT sigla,nome  FROM `basedosdados.br_bd_diretorios_brasil.uf`) AS diretorio_sigla_uf
    ON dados.sigla_uf = diretorio_sigla_uf.sigla
LEFT JOIN `dicionario_capital`
    ON dados.capital = chave_capital
LEFT JOIN `dicionario_v1022`
    ON dados.v1022 = chave_v1022
LEFT JOIN `dicionario_a003`
    ON dados.a003 = chave_a003
LEFT JOIN `dicionario_a005`
    ON dados.a005 = chave_a005
LEFT JOIN `dicionario_b0011`
    ON dados.b0011 = chave_b0011
LEFT JOIN `dicionario_b0012`
    ON dados.b0012 = chave_b0012
LEFT JOIN `dicionario_b0013`
    ON dados.b0013 = chave_b0013
LEFT JOIN `dicionario_b0015`
    ON dados.b0015 = chave_b0015
LEFT JOIN `dicionario_b00111`
    ON dados.b00111 = chave_b00111
LEFT JOIN `dicionario_b002`
    ON dados.b002 = chave_b002
LEFT JOIN `dicionario_b0033`
    ON dados.b0033 = chave_b0033
LEFT JOIN `dicionario_b0034`
    ON dados.b0034 = chave_b0034
LEFT JOIN `dicionario_b0035`
    ON dados.b0035 = chave_b0035
LEFT JOIN `dicionario_b005`
    ON dados.b005 = chave_b005
LEFT JOIN `dicionario_b006`
    ON dados.b006 = chave_b006
LEFT JOIN `dicionario_b007`
    ON dados.b007 = chave_b007
LEFT JOIN `dicionario_b009a`
    ON dados.b009a = chave_b009a
LEFT JOIN `dicionario_b009b`
    ON dados.b009b = chave_b009b
LEFT JOIN `dicionario_c001`
    ON dados.c001 = chave_c001
LEFT JOIN `dicionario_c002`
    ON dados.c002 = chave_c002
LEFT JOIN `dicionario_c003`
    ON dados.c003 = chave_c003
LEFT JOIN `dicionario_c005`
    ON dados.c005 = chave_c005
LEFT JOIN `dicionario_c007c`
    ON dados.c007c = chave_c007c
LEFT JOIN `dicionario_c01011`
    ON dados.c01011 = chave_c01011
LEFT JOIN `dicionario_c013`
    ON dados.c013 = chave_c013
LEFT JOIN `dicionario_f001`
    ON dados.f001 = chave_f001
LEFT JOIN `dicionario_f0022`
    ON dados.f0022 = chave_f0022
"""

df_pnad = pd.read_sql(query = query)

df_pnad.to_parquet("pnad_covid_amostra.parquet", index=False)