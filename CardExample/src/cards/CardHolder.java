package cards;

import java.util.ArrayList;

public class CardHolder {
	private ArrayList<Card>cards;

	public CardHolder(Card c1,Card c2)
	{
		cards=new ArrayList<Card>();
		cards.add(c1);
		cards.add(c2);
	}
	/**
	 * <pre>
	 * adds card in place of null spot in list in no spot does nothing
	 * -----------------------------------------------------------------
	 * cards.addCard(card);
	 * <pre>
	 * @return
	 */
	public void addCard(Card cardIn)
	{
		if(cards.get(0)==null)
		{
			cards.set(0, cardIn);
		}
		else if(cards.get(1)==null)
		{
			cards.set(1, cardIn);
		}
	}
	/**
	 * <pre>
	 * formats cards in list and returns String
	 * ------------------------------------------------------
	 * String output=cards.formatCards();
	 * <pre>
	 * @return
	 */
	public String formatCards()
	{
		String out="";
		for(Card card:cards)
		{
			out=out+card.toString()+"\n\n";
		}
		return out;
	}
}
