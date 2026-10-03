"""
🌟 JOGUINHO INFANTIL - PEGA ESTRELAS! 🌟
=========================================
Use as setas ← → para mover o cestinho e pegar as estrelas!
Cuidado com os raios ⚡ — eles tiram pontos!

Como rodar:
1. Instale o pygame: pip install pygame
2. Execute: python joguinho_infantil.py
"""

import pygame
import random
import sys
import math

# ============================================================
# CONFIGURAÇÕES DO JOGO
# ============================================================
LARGURA = 800
ALTURA = 600
FPS = 60

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL_CLARO = (135, 206, 235)
AZUL_ESCURO = (25, 25, 112)
AMARELO = (255, 215, 0)
LARANJA = (255, 165, 0)
VERMELHO = (255, 69, 0)
VERDE = (34, 139, 34)
VERDE_CLARO = (144, 238, 144)
ROSA = (255, 105, 180)
ROXO = (148, 103, 226)
MARROM = (139, 90, 43)
MARROM_CLARO = (205, 133, 63)
CINZA = (200, 200, 200)

# ============================================================
# FUNÇÕES DE DESENHO
# ============================================================

def desenhar_estrela(tela, cor, centro_x, centro_y, tamanho):
    """Desenha uma estrela de 5 pontas."""
    pontos = []
    for i in range(10):
        angulo = math.radians(i * 36 - 90)
        if i % 2 == 0:
            raio = tamanho
        else:
            raio = tamanho * 0.4
        x = centro_x + raio * math.cos(angulo)
        y = centro_y + raio * math.sin(angulo)
        pontos.append((x, y))
    pygame.draw.polygon(tela, cor, pontos)
    # Brilho
    cor_brilho = tuple(min(c + 60, 255) for c in cor)
    pontos_brilho = []
    for i in range(10):
        angulo = math.radians(i * 36 - 90)
        if i % 2 == 0:
            raio = tamanho * 0.6
        else:
            raio = tamanho * 0.25
        x = centro_x + raio * math.cos(angulo)
        y = centro_y + raio * math.sin(angulo)
        pontos_brilho.append((x, y))
    pygame.draw.polygon(tela, cor_brilho, pontos_brilho)


def desenhar_raio(tela, centro_x, centro_y, tamanho):
    """Desenha um raio (obstáculo)."""
    pontos = [
        (centro_x - tamanho * 0.3, centro_y - tamanho),
        (centro_x + tamanho * 0.1, centro_y - tamanho * 0.2),
        (centro_x + tamanho * 0.4, centro_y - tamanho * 0.3),
        (centro_x + tamanho * 0.05, centro_y + tamanho * 0.3),
        (centro_x + tamanho * 0.3, centro_y + tamanho * 0.2),
        (centro_x - tamanho * 0.15, centro_y + tamanho),
        (centro_x, centro_y + tamanho * 0.2),
        (centro_x - tamanho * 0.35, centro_y + tamanho * 0.3),
    ]
    pygame.draw.polygon(tela, AMARELO, pontos)
    pygame.draw.polygon(tela, LARANJA, pontos, 2)


def desenhar_cestinho(tela, x, y, largura_cesta, altura_cesta):
    """Desenha um cestinho bonito."""
    # Corpo do cesto
    pontos_cesto = [
        (x - largura_cesta // 2, y - altura_cesta),
        (x + largura_cesta // 2, y - altura_cesta),
        (x + largura_cesta // 2 - 10, y),
        (x - largura_cesta // 2 + 10, y),
    ]
    pygame.draw.polygon(tela, MARROM, pontos_cesto)
    pygame.draw.polygon(tela, MARROM_CLARO, pontos_cesto, 3)

    # Linhas decorativas no cesto
    for i in range(1, 4):
        y_linha = y - altura_cesta + i * (altura_cesta // 4)
        margem = 10 * (i / 4)
        pygame.draw.line(
            tela, MARROM_CLARO,
            (x - largura_cesta // 2 + int(margem) + 3, y_linha),
            (x + largura_cesta // 2 - int(margem) - 3, y_linha),
            2
        )

    # Alça do cesto
    pygame.draw.arc(
        tela, MARROM,
        (x - largura_cesta // 3, y - altura_cesta - 20, largura_cesta * 2 // 3, 30),
        0, math.pi, 3
    )


def desenhar_coracao(tela, cor, cx, cy, tamanho):
    """Desenha um coração para as vidas."""
    t = tamanho
    pygame.draw.circle(tela, cor, (cx - t // 4, cy - t // 6), t // 3)
    pygame.draw.circle(tela, cor, (cx + t // 4, cy - t // 6), t // 3)
    pontos = [
        (cx - t // 2 - 2, cy - t // 8),
        (cx, cy + t // 2),
        (cx + t // 2 + 2, cy - t // 8),
    ]
    pygame.draw.polygon(tela, cor, pontos)


def desenhar_fundo(tela, tempo):
    """Desenha o fundo do jogo com gradiente e nuvens."""
    # Gradiente de céu
    for y in range(ALTURA):
        r = int(135 - (y / ALTURA) * 60)
        g = int(206 - (y / ALTURA) * 80)
        b = int(250 - (y / ALTURA) * 50)
        pygame.draw.line(tela, (max(r, 0), max(g, 0), max(b, 0)), (0, y), (LARGURA, y))

    # Chão (grama)
    pygame.draw.rect(tela, VERDE, (0, ALTURA - 60, LARGURA, 60))
    pygame.draw.rect(tela, VERDE_CLARO, (0, ALTURA - 60, LARGURA, 8))

    # Nuvens que se movem
    deslocamento = (tempo * 0.02) % (LARGURA + 200)
    for nx, ny in [(100, 60), (350, 40), (600, 70), (200, 100)]:
        pos_x = (nx + int(deslocamento)) % (LARGURA + 200) - 100
        pygame.draw.ellipse(tela, BRANCO, (pos_x, ny, 100, 40))
        pygame.draw.ellipse(tela, BRANCO, (pos_x + 25, ny - 15, 60, 35))
        pygame.draw.ellipse(tela, BRANCO, (pos_x + 50, ny, 80, 35))


def desenhar_particula(tela, x, y, cor, tamanho):
    """Desenha uma partícula de efeito."""
    pygame.draw.circle(tela, cor, (int(x), int(y)), max(int(tamanho), 1))


# ============================================================
# CLASSES DO JOGO
# ============================================================

class Estrela:
    """Objeto que cai — estrela (boa) ou raio (ruim)."""

    CORES_ESTRELA = [AMARELO, LARANJA, ROSA, ROXO, (0, 200, 255)]

    def __init__(self, tipo="estrela"):
        self.tipo = tipo  # "estrela" ou "raio"
        self.x = random.randint(40, LARGURA - 40)
        self.y = random.randint(-100, -20)
        self.tamanho = random.randint(15, 22)
        self.velocidade = random.uniform(2.0, 4.5)
        self.cor = random.choice(self.CORES_ESTRELA)
        self.angulo = 0
        self.balanco = random.uniform(-0.5, 0.5)

    def atualizar(self):
        self.y += self.velocidade
        self.x += math.sin(self.angulo) * self.balanco
        self.angulo += 0.05
        # Manter dentro da tela
        self.x = max(20, min(LARGURA - 20, self.x))

    def desenhar(self, tela):
        if self.tipo == "estrela":
            desenhar_estrela(tela, self.cor, int(self.x), int(self.y), self.tamanho)
        else:
            desenhar_raio(tela, int(self.x), int(self.y), self.tamanho)

    def fora_da_tela(self):
        return self.y > ALTURA + 20


class Particula:
    """Efeito visual ao pegar uma estrela."""

    def __init__(self, x, y, cor):
        self.x = x
        self.y = y
        self.cor = cor
        self.vx = random.uniform(-3, 3)
        self.vy = random.uniform(-5, -1)
        self.vida = random.randint(15, 30)
        self.tamanho = random.uniform(2, 5)

    def atualizar(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.15  # gravidade
        self.vida -= 1
        self.tamanho *= 0.95

    def viva(self):
        return self.vida > 0

    def desenhar(self, tela):
        desenhar_particula(tela, self.x, self.y, self.cor, self.tamanho)


class Jogador:
    """O cestinho controlado pelo jogador."""

    def __init__(self):
        self.x = LARGURA // 2
        self.y = ALTURA - 80
        self.largura = 80
        self.altura = 45
        self.velocidade = 7

    def mover(self, teclas):
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.x -= self.velocidade
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.x += self.velocidade
        # Limites
        self.x = max(self.largura // 2, min(LARGURA - self.largura // 2, self.x))

    def desenhar(self, tela):
        desenhar_cestinho(tela, self.x, self.y, self.largura, self.altura)

    def colidiu(self, obj):
        dist_x = abs(self.x - obj.x)
        dist_y = abs(self.y - self.altura // 2 - obj.y)
        return dist_x < self.largura // 2 + 5 and dist_y < self.altura // 2 + obj.tamanho


# ============================================================
# JOGO PRINCIPAL
# ============================================================

class Jogo:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("🌟 Pega Estrelas! 🌟")
        self.relogio = pygame.time.Clock()

        # Fontes
        self.fonte_grande = pygame.font.SysFont("Arial", 52, bold=True)
        self.fonte_media = pygame.font.SysFont("Arial", 32, bold=True)
        self.fonte_pequena = pygame.font.SysFont("Arial", 22)
        self.fonte_pontos = pygame.font.SysFont("Arial", 28, bold=True)

        self.reiniciar()

    def reiniciar(self):
        self.jogador = Jogador()
        self.objetos = []
        self.particulas = []
        self.pontos = 0
        self.vidas = 3
        self.tempo_jogo = 0
        self.intervalo_spawn = 50  # frames entre spawns
        self.contador_spawn = 0
        self.game_over = False
        self.recorde = 0
        self.nivel = 1

    def spawn_objeto(self):
        """Cria novos objetos caindo."""
        self.contador_spawn += 1
        if self.contador_spawn >= self.intervalo_spawn:
            self.contador_spawn = 0
            # Chance de raio aumenta com o nível
            chance_raio = min(0.15 + self.nivel * 0.03, 0.35)
            if random.random() < chance_raio:
                self.objetos.append(Estrela("raio"))
            else:
                self.objetos.append(Estrela("estrela"))

    def criar_particulas(self, x, y, cor, quantidade=10):
        """Cria efeito de partículas."""
        for _ in range(quantidade):
            self.particulas.append(Particula(x, y, cor))

    def atualizar(self):
        if self.game_over:
            return

        self.tempo_jogo += 1

        # Atualizar nível (a cada 15 pontos)
        self.nivel = 1 + self.pontos // 15

        # Ajustar dificuldade
        self.intervalo_spawn = max(20, 50 - self.nivel * 3)

        # Mover jogador
        teclas = pygame.key.get_pressed()
        self.jogador.mover(teclas)

        # Spawnar objetos
        self.spawn_objeto()

        # Atualizar objetos
        for obj in self.objetos[:]:
            obj.atualizar()

            # Colisão com jogador
            if self.jogador.colidiu(obj):
                if obj.tipo == "estrela":
                    self.pontos += 1
                    self.criar_particulas(obj.x, obj.y, obj.cor, 12)
                else:
                    self.vidas -= 1
                    self.criar_particulas(obj.x, obj.y, VERMELHO, 8)
                    if self.vidas <= 0:
                        self.game_over = True
                        self.recorde = max(self.recorde, self.pontos)
                self.objetos.remove(obj)
                continue

            # Remover se saiu da tela
            if obj.fora_da_tela():
                self.objetos.remove(obj)

        # Atualizar partículas
        for p in self.particulas[:]:
            p.atualizar()
            if not p.viva():
                self.particulas.remove(p)

    def desenhar_hud(self):
        """Desenha pontuação, vidas e nível."""
        # Fundo do HUD
        s = pygame.Surface((LARGURA, 45))
        s.set_alpha(120)
        s.fill(PRETO)
        self.tela.blit(s, (0, 0))

        # Pontos
        texto_pontos = self.fonte_pontos.render(f"⭐ Pontos: {self.pontos}", True, BRANCO)
        self.tela.blit(texto_pontos, (15, 8))

        # Nível
        texto_nivel = self.fonte_pequena.render(f"Nível {self.nivel}", True, AMARELO)
        self.tela.blit(texto_nivel, (LARGURA // 2 - texto_nivel.get_width() // 2, 12))

        # Vidas (corações)
        for i in range(self.vidas):
            desenhar_coracao(self.tela, VERMELHO, LARGURA - 40 - i * 40, 22, 24)

    def desenhar_game_over(self):
        """Tela de Game Over."""
        # Overlay escuro
        s = pygame.Surface((LARGURA, ALTURA))
        s.set_alpha(150)
        s.fill(PRETO)
        self.tela.blit(s, (0, 0))

        # Textos
        texto_fim = self.fonte_grande.render("FIM DE JOGO!", True, VERMELHO)
        self.tela.blit(texto_fim, (LARGURA // 2 - texto_fim.get_width() // 2, 180))

        texto_pontos = self.fonte_media.render(f"Você fez {self.pontos} pontos!", True, AMARELO)
        self.tela.blit(texto_pontos, (LARGURA // 2 - texto_pontos.get_width() // 2, 260))

        texto_nivel = self.fonte_pequena.render(f"Chegou no Nível {self.nivel}", True, BRANCO)
        self.tela.blit(texto_nivel, (LARGURA // 2 - texto_nivel.get_width() // 2, 310))

        # Mensagem motivacional
        if self.pontos < 10:
            msg = "Continue tentando! Você consegue! 💪"
        elif self.pontos < 25:
            msg = "Muito bom! Está melhorando! 🎉"
        elif self.pontos < 50:
            msg = "Incrível! Você é demais! 🌟"
        else:
            msg = "CAMPEÃO(Ã)! Nota 10! 🏆"
        texto_msg = self.fonte_pequena.render(msg, True, VERDE_CLARO)
        self.tela.blit(texto_msg, (LARGURA // 2 - texto_msg.get_width() // 2, 360))

        texto_reiniciar = self.fonte_pequena.render(
            "Pressione ESPAÇO para jogar de novo  |  ESC para sair", True, CINZA
        )
        self.tela.blit(texto_reiniciar, (LARGURA // 2 - texto_reiniciar.get_width() // 2, 430))

    def desenhar_tela_inicial(self):
        """Tela de início (não usada neste fluxo, mas disponível)."""
        pass

    def desenhar(self):
        # Fundo
        desenhar_fundo(self.tela, self.tempo_jogo)

        # Objetos caindo
        for obj in self.objetos:
            obj.desenhar(self.tela)

        # Partículas
        for p in self.particulas:
            p.desenhar(self.tela)

        # Jogador
        self.jogador.desenhar(self.tela)

        # HUD
        self.desenhar_hud()

        # Game Over
        if self.game_over:
            self.desenhar_game_over()

        pygame.display.flip()

    def rodar(self):
        """Loop principal do jogo."""
        rodando = True
        while rodando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        rodando = False
                    if evento.key == pygame.K_SPACE and self.game_over:
                        self.reiniciar()

            self.atualizar()
            self.desenhar()
            self.relogio.tick(FPS)

        pygame.quit()
        sys.exit()


# ============================================================
# INICIAR O JOGO
# ============================================================
if __name__ == "__main__":
    jogo = Jogo()
    jogo.rodar()
