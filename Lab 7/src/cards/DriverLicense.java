package cards;

import java.util.Calendar;

public class DriverLicense extends IDCard{
	private String State;
	private int experationDate;
	
	public DriverLicense(String name, int IDIn, String stateIn, int dateExpire)
	{
		super(IDIn,name);
		State = stateIn;
		experationDate=dateExpire;
	}
	/**
	 * <pre>
	 * formats into String
	 * ------------------------------------------------------
	 * String output=DriverLicense.toString();
	 * <pre>
	 * @return
	 */
	public String toString()
	{
		return "Card Type: "+this.getClass().getSimpleName()+"\nCard Holder: "+super.getName()+"\nID Number: "+super.getIDNumber()+"\nState: "+State+"\nExpiration Year: "+experationDate;
	}
	/**
	 * <pre>
	 * tests to see if license is expired
	 * ------------------------------------------------------
	 * boolean yesNo = DriverLicense.isExpired();
	 * <pre>
	 * @return
	 */
	@Override
	public boolean isExpired()
	   {
	      Calendar now = Calendar.getInstance();
	      
	      int year = now.get(Calendar.YEAR);
	      
	      if(experationDate<year)
	      {
	    	  return true;
	      }
	      else
	      {
	    	  return false;
	      }
	      
	   }
}
