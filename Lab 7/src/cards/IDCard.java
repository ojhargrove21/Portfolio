package cards;

public class IDCard extends Card{
	private int IDNumber;

	public IDCard(int IDNum,String name)
	{
		super(name);
		IDNumber=IDNum;
	}
	/**
	 * <pre>
	 * returns ID number
	 * ------------------------------------------------------
	 * int ID=IDCard.getIDNumber();
	 * <pre>
	 * @return
	 */
	public int getIDNumber()
	{
		return IDNumber;
	}
	/**
	 * <pre>
	 * formats into String
	 * ------------------------------------------------------
	 * String output=IDCard.toString();
	 * <pre>
	 * @return
	 */
	public String toString()
	{
		return "Card Type: "+this.getClass().getSimpleName()+"\nCard Holder: "+super.getName()+"\nID Number: "+IDNumber;
	}
}
