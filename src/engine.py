from state import Piece, Board, GameMove, GameState, ROLL_DICE
from util import roll as roll_dice
from typing import List, Sequence


class Dice:
    def roll(self) -> int:
        return roll_dice()


class GameEngine:
    def __init__(self, board: Board, dice: Dice = Dice()):
        self.state = GameState.create(board)
        self.dice = dice

    def get_state(self) -> GameState:
        return self.state

    def __next_player(self) -> int:
        current_player_index = self.state.board.players.index(self.state.current_player)
        if current_player_index >= (len(self.state.board.players) - 1):
            current_player_index = 0
            return self.state.board.players[0]
        return self.state.board.players[current_player_index + 1]

    def __on_roll_dice(self, player: int) -> GameState:
        dice = self.dice.roll()
        self.state.dice = dice
        player = self.state.current_player
        valid_actions: List[GameMove] = []

        def calc_valid_actions(piece: Piece) -> None:
            if self.state.board.is_on_start(piece) and dice == 6:
                valid_actions.append(GameMove.piece_out(player, piece.number, dice))
            # elif self.state.board.is_on_path(piece):

        for piece in self.state.board.pieces:
            if piece.player == player:
                calc_valid_actions(piece)
        if len(valid_actions) == 0:
            next_player = self.__next_player()
            self.state.current_player = next_player
            valid_actions.append(GameMove.roll_dice(next_player))

        self.state.valid_actions = valid_actions
        self.state.number = self.state.number + 1
        return self.state

    def __on_piece_out(self, player: int, piece: Piece, dice: int) -> GameState:
        pass

    def __on_move_piece(self, player: int, piece: Piece, dice: int) -> GameState:
        pass

    def play(self, move: GameMove) -> GameState:
        if move not in self.state.valid_actions:
            raise ValueError(
                f"Illegal action {move} is not one of {self.state.valid_actions}"
            )

        if move.move_type == ROLL_DICE:
            self.__on_roll_dice(move.player)

        return self.state
