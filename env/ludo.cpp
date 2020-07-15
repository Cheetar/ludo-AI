#include <iostream>
#include <string.h>
#include <time.h>
#include <cassert>

using namespace std;

int const NO_PAWNS = 4;
int const NO_PLAYERS = 4;
int const REROLL = 6;
int const NORMAL_SQUARES = 13 * 4;
int const HOME_SIZE = 4;
int const NULL_MOVE = 0;

// State is 17 numbers that defines current game state (16 pawns and dice roll)
typedef int* state;
// Action is defined by one number - which pawn is moved. 0 means pass move
typedef int action;


class Ludo {
  int pawns[NO_PLAYERS + 1][NO_PAWNS + 1] = {0};
  int dice;
  int turn;
  int player_to_move;

  private:
    static int diceRoll() {
      return rand() % 6 + 1;
    }

  public:
    Ludo() {
      initialize();
    }

    void initialize() {
      for (int i = 1; i <= NO_PLAYERS; i++)
        for (int j = 1; j <= NO_PAWNS; j++)
          pawns[i][j] = 0;
      dice = diceRoll();
      turn = 0;
      player_to_move = 1;
    }

    void getState() {
      cout << turn << " ";
      cout << dice << " ";
      cout << player_to_move << " |";
      for (int i = 1; i <= NO_PLAYERS; i++) {
        for (int j = 1; j <= NO_PAWNS; j++) {
          cout << pawns[i][j] << " ";
        }
        cout << "|";
      }
      cout << "\n";
    }

    bool execAction(action a) {
      assert(isActionValid(a));

      if (a != 0) {
        if (pawns[player_to_move][a] == 0)
          pawns[player_to_move][a] = 1;
        else
          pawns[player_to_move][a] += dice;

        int pos = pawns[player_to_move][a];
        for (int p = 1; p <= NO_PLAYERS; p++)
          for (int i = 1; i <= NO_PAWNS; i++)
            if (p != player_to_move &&
                i != a &&
                pawns[p][i] > 0 &&
                pawns[p][i] <= NORMAL_SQUARES &&
                pos == pawns[p][i] + (NORMAL_SQUARES * (p - player_to_move)))
                pawns[p][i] = 0; // Takedown
      }

      if (dice != REROLL) {
        turn += 1;
        player_to_move = (player_to_move % NO_PLAYERS) + 1;
      }
      dice = diceRoll();
    }

    bool isActionValid(action a) {
      if (a != NULL_MOVE) {
        int pos = pawns[player_to_move][a];
        if (pos == 0)
          return dice == REROLL;

        // Not exceed the board
        if (pos + dice <= NORMAL_SQUARES + HOME_SIZE) {
            for (int i = 1; i <= NO_PAWNS; i++) {
              if (i != a) {
                // Not jumping over other pawns at home
                if (pawns[player_to_move][i] > pos &&
                    pawns[player_to_move][i] <= pos + dice &&
                    pawns[player_to_move][i] > NORMAL_SQUARES)
                    return false;
              }
            }
            return true;
        }
        return false;
      } else {
        return (!isActionValid(1) &&
                !isActionValid(2) &&
                !isActionValid(3) &&
                !isActionValid(4));
      }
    }

    action getRandomAction() {
      for (int i = 0; i <= NO_PAWNS; i++)
        if (isActionValid(i))
          return i;
    }

    bool hasGameEnded() {
      for (int p = 1; p <= NO_PLAYERS; p++)
        for (int j = 1; j <= NO_PAWNS; j++)
          if (pawns[p][j] <= NORMAL_SQUARES)
            return false;
      return true;
    }

};


int main(int argc, char *argv[]) {
  srand( (unsigned)time(NULL) );

  Ludo env = Ludo();
  for (int i = 0; i < 100000000; i++) {
    while (!env.hasGameEnded()) {
      // env.getState();  <- For debugging purposes
      action a = env.getRandomAction();
      env.execAction(a);
    }
  }
}
