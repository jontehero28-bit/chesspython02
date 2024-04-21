import pygame
import sys

#Initialize
pygame.init()

#Initial variables
width = height = 512 #squares 64pixels
dimension = 8  #chessboard size squares 8x8
squareSize = height// dimension #8x8 = 64 512/8 = 8
images = {}

#color
#use colors from pygame instead

#images

def loadImages():  #name of the piece matches the name of the image
    pieces = ["wP", "wR", "wN", "wB", "wK", "wQ", "wB", "wN", "wR", "bP", "bR", "bN", "bB", "bK", "bQ", "bB", "bN", "bR"]
    for piece in pieces: #scale images to square size    
        images[piece] = pygame.transform.scale(pygame.image.load("images/" + piece + ".png"), (squareSize, squareSize))

class ChessPiece:     #represent common functionality of all chess pieces
    def __init__(self, symbol, color, imageLoad):
        self.color = color
        self.symbol = symbol
        self.image = pygame.image.load("images/" + imageLoad)
        
        #currentPosition
        #self.currentPosition = currentPosition
        #self.letter = currentPosition[0]
        #self.letter = currentPosition[1]
        #self.possibleMoves = []
        
    def get_symbol(self):
        return self.symbol

    def get_color(self):
        return self.color

    def get_image(self):
        return self.image
    

#fill up data for the all of the pieces
whiteKilled = []
blackKilled = []

#helper function creates every piece for whites and blacks.

def createChessPieces(color):
    pieces = ["P", "R", "N", "B", "K", "Q"]
    firstLetter = 'w' if color == "white" else 'b'
    
    # Create and return a list of ChessPiece instances making it much shorter
    return [
        ChessPiece(f"{firstLetter}{p}", color, f"{firstLetter}{p}.png") 
        for p in pieces
        ]

whitePieces = createChessPieces("white")
blackPieces = createChessPieces("black")
    

class ChessBoard:
    def __init__(self):
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR",],   
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP",],
            ["--", "--", "--", "--", "--", "--", "--", "--",],
            ["--", "--", "--", "--", "--", "--", "--", "--",],
            ["--", "--", "--", "--", "--", "--", "--", "--",],
            ["--", "--", "--", "--", "--", "--", "--", "--",],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP",],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR",]]
        self.whiteTurnMove = True
        self.moveLog = []
    
        
def main():
    ch = ChessBoard()   #for chessboard class
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Chess")
    fps = 30
    time = pygame.time.Clock()
    
    loadImages()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        #draw and update        
        drawBoard(screen)
        drawPieces(screen, ch.board)
        time.tick(fps)        
        pygame.display.flip()
        
        
def drawBoard(screen):
    colors = [pygame.Color("beige"), pygame.Color("dark green")]      
    for r in range(dimension): #for 8 rows (dimension = 8)
        for c in range(dimension): #for 8 columns
            color = colors[((r+c)%2)]  #chatGPT hepled me here, (from chatGPT) color = BOARD_COLOR_1 if (row + col) % 2 == 0 else BOARD_COLOR_2v
            pygame.draw.rect(screen, color, pygame.Rect(c*squareSize, r*squareSize, squareSize, squareSize))

def drawPieces(screen, board):
    for r in range(dimension):
        for c in range(dimension):
            piece = board[r][c]
            if piece != "--":
                screen.blit(images[piece], pygame.Rect(c*squareSize, r*squareSize, squareSize, squareSize))


if __name__ == '__main__':
    main()
    
